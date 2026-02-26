from __future__ import annotations

from pathlib import Path
import re

from src.utils import DAY_LABELS_KO, DAY_ORDER, join_non_empty, normalize_space


def _escape_md_text(text: str) -> str:
    # Escape markdown-significant characters that can break table rendering
    # or create unintended emphasis in GitHub README.
    escaped = text.replace("\\", "\\\\")
    escaped = (
        escaped.replace("|", "\\|")
        .replace("_", "\\_")
        .replace("*", "\\*")
        .replace("~", "\\~")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )
    return escaped


def _is_unavailable_text(text: str) -> bool:
    t = normalize_space(text).replace(".", "")
    return t in {"미운영", "*", ""}


def _format_price(price: str) -> str:
    p = normalize_space(price)
    if not p:
        return ""
    digits = "".join(ch for ch in p if ch.isdigit())
    if not digits:
        return p
    return f"{int(digits):,}원"


def _format_item_with_price(item: dict) -> str:
    name = normalize_space(item.get("name", ""))
    raw_price = normalize_space(str(item.get("price", "")))
    price = _format_price(raw_price)
    if not name or _is_unavailable_text(name):
        return ""
    safe_name = _escape_md_text(name)
    if price:
        return f"{safe_name} ({_escape_md_text(price)})"
    return safe_name


def _category_emoji(category: str) -> str:
    c = normalize_space(category)
    if "조식" in c or "아침" in c:
        return "🌄"
    if "중식" in c or "점심" in c:
        return "☀️"
    if "석식" in c or "저녁" in c:
        return "🌛"
    return ""


def _format_yonsei_entries(entries: list[dict]) -> str:
    lines: list[str] = []
    for section in entries:
        category = normalize_space(section.get("category", ""))
        raw_items = section.get("items", [])

        visible_items = [
            formatted
            for formatted in (_format_item_with_price(i) for i in raw_items)
            if formatted
        ]

        safe_category = _escape_md_text(category)
        title = f"**{safe_category}**" if safe_category else "**메뉴**"
        icon = _category_emoji(category)
        if visible_items:
            line = f"{title}: {', '.join(visible_items)}"
            lines.append(f"{icon} {line}" if icon else line)
            continue

        had_unavailable = any(
            _is_unavailable_text(normalize_space(i.get("name", ""))) for i in raw_items
        )
        if had_unavailable:
            line = f"{title}: 미운영"
            lines.append(f"{icon} {line}" if icon else line)

    return "<br>".join(lines) if lines else "-"


MEAL_EMOJI = {
    "조식": "🌄",
    "중식": "☀️",
    "석식": "🌛",
}


def _meal_emoji(meal: str) -> str:
    return MEAL_EMOJI.get(meal, "")


def _format_aramark_entries(entries: list[dict]) -> str:
    lines: list[str] = []
    for entry in entries:
        meal_raw = normalize_space(entry.get("meal_time", ""))
        meal = _escape_md_text(meal_raw)
        category = _escape_md_text(normalize_space(entry.get("category", "")))
        items = [_escape_md_text(normalize_space(i)) for i in entry.get("items", [])]
        menu = ", ".join([i for i in items if i]) if items else "-"
        prefix = join_non_empty([meal, category], " · ")
        icon = _meal_emoji(meal_raw)
        if prefix:
            line = f"**{prefix}**: {menu}"
        else:
            line = menu
        lines.append(f"{icon} {line}" if icon else line)
    return "<br>".join(lines) if lines else "-"


def _day_label(day_key: str, week_labels: dict[str, str]) -> str:
    return week_labels.get(day_key) or DAY_LABELS_KO.get(day_key, day_key)


def _build_week_table(
    week: dict[str, list[dict]], formatter, week_labels: dict[str, str]
) -> str:
    lines = ["| 요일(날짜) | 메뉴 |", "|---|---|"]
    for day_key in DAY_ORDER:
        day_label = _day_label(day_key, week_labels)
        value = formatter(week.get(day_key, []))
        lines.append(f"| {day_label} | {value} |")
    return "\n".join(lines)


def _build_day_table(day_key: str, day_label: str, rows: list[tuple[str, str]]) -> str:
    lines = [f"<a id=\"day-{day_key}\"></a>", f"### {day_label}", "", "| 식당 | 메뉴 |", "|---|---|"]
    for restaurant, menu in rows:
        safe_restaurant = _escape_md_text(restaurant)
        lines.append(f"| {safe_restaurant} | {menu or '-'} |")
    return "\n".join(lines)


def _find_restaurant(restaurants: list[dict], target_name: str) -> dict | None:
    for r in restaurants:
        if r.get("name") == target_name:
            return r
    return None


def _fallback_table(message: str) -> str:
    return "\n".join(["| 요일(날짜) | 메뉴 |", "|---|---|", f"| - | {message} |"])


def _menu_count(rest: dict | None) -> int:
    if not rest:
        return 0
    return sum(len(rest.get("week", {}).get(day, [])) for day in DAY_ORDER)


def _format_operating_hours(rest: dict | None) -> str:
    if not rest:
        return "-"

    raw = (rest.get("operating_hours", "") or "").replace("\r", "")
    if not raw.strip():
        return "-"

    lines = [normalize_space(line) for line in raw.split("\n") if normalize_space(line)]
    if not lines:
        return "-"

    grouped: dict[str, dict[str, list[str]]] = {
        "학기중": {"평일": [], "주말": [], "기타": []},
        "방학중": {"평일": [], "주말": [], "기타": []},
        "기타": {"평일": [], "주말": [], "기타": []},
    }

    def classify_day(line: str) -> str | None:
        if "평일" in line:
            return "평일"
        if any(tok in line for tok in ["토요일", "일요일", "주말", "공휴일"]):
            return "주말"
        return None

    current_period = "기타"
    current_day = "기타"

    for line in lines:
        # Pattern like: "1층 운영시간 : 학기중(...), 방학중(...)"
        dual = re.match(
            r"^(.*?)(?:\s*[:：]\s*)?학기중\(([^)]*)\)\s*,?\s*방학중\(([^)]*)\)\s*$",
            line,
        )
        if dual:
            label = normalize_space(dual.group(1)) or "운영시간"
            grouped["학기중"]["기타"].append(f"{label}: {normalize_space(dual.group(2))}")
            grouped["방학중"]["기타"].append(f"{label}: {normalize_space(dual.group(3))}")
            continue

        if "학기중" in line:
            current_period = "학기중"
            remainder = normalize_space(
                re.sub(r"[■\-\s]*학기중\s*운영시간?\s*", "", line)
            )
            if remainder:
                grouped[current_period][current_day].append(remainder)
            continue

        if "방학중" in line:
            current_period = "방학중"
            remainder = normalize_space(
                re.sub(r"[■\-\s]*방학중\s*운영시간?\s*", "", line)
            )
            if remainder:
                grouped[current_period][current_day].append(remainder)
            continue

        day_key = classify_day(line)
        if day_key:
            current_day = day_key
            # For sentence-style policy lines, preserve original text.
            if any(tok in line for tok in ["휴무", "변경", "안내"]):
                grouped[current_period][current_day].append(line)
                continue

            remainder = line
            for token in ["평일", "토요일", "일요일", "주말", "공휴일"]:
                remainder = remainder.replace(token, "")
            remainder = normalize_space(remainder.strip(" :,-"))
            if remainder:
                grouped[current_period][current_day].append(remainder)
            continue

        grouped[current_period][current_day].append(line)

    # Render with explicit hierarchy: 학기중/방학중 → 평일/주말
    rendered: list[str] = []
    for period in ["학기중", "방학중", "기타"]:
        block = grouped[period]
        has_content = any(block[k] for k in ["평일", "주말", "기타"])
        if not has_content:
            continue

        if period != "기타":
            rendered.append(f"**{_escape_md_text(period)}**")

        for day_key in ["평일", "주말"]:
            items = block[day_key]
            if not items:
                continue
            rendered.append(f"- {_escape_md_text(day_key)}")
            for item in items:
                rendered.append(f"  - {_escape_md_text(item)}")

        for item in block["기타"]:
            rendered.append(f"- {_escape_md_text(item)}")

    return "\n".join(rendered) if rendered else "-"


def render_readme(data: dict, template_path: Path) -> str:
    template = template_path.read_text(encoding="utf-8")

    yonsei_restaurants = data.get("yonsei_university", {}).get("restaurants", [])
    aramark_restaurants = data.get("severance_aramark", {}).get("restaurants", [])
    week_labels = data.get("week_labels", {})

    manna = _find_restaurant(yonsei_restaurants, "맛나샘")
    eoulsam = _find_restaurant(yonsei_restaurants, "어울샘(한경관)")
    jonghap = _find_restaurant(aramark_restaurants, "종합관")
    jejung = _find_restaurant(aramark_restaurants, "제중관")

    day_sections: list[str] = []
    for day_key in DAY_ORDER:
        day_label = _day_label(day_key, week_labels)
        rows = [
            (
                "연세대학교 맛나샘",
                _format_yonsei_entries(manna.get("week", {}).get(day_key, []))
                if manna
                else "-",
            ),
            (
                "연세대학교 한경관(어울샘)",
                _format_yonsei_entries(eoulsam.get("week", {}).get(day_key, []))
                if eoulsam
                else "-",
            ),
            (
                "세브란스 종합관",
                _format_aramark_entries(jonghap.get("week", {}).get(day_key, []))
                if jonghap
                else "-",
            ),
            (
                "세브란스 제중관",
                _format_aramark_entries(jejung.get("week", {}).get(day_key, []))
                if jejung
                else "-",
            ),
        ]
        day_sections.append(_build_day_table(day_key, day_label, rows))

    day_quick_links = " | ".join(
        [f"[{_day_label(day, week_labels)}](#day-{day})" for day in DAY_ORDER]
    )

    operating_hours_section = "\n\n".join(
        [
            "### 연세대학교 맛나샘\n" + _format_operating_hours(manna),
            "### 연세대학교 한경관(어울샘)\n" + _format_operating_hours(eoulsam),
            "### 세브란스 종합관\n" + _format_operating_hours(jonghap),
            "### 세브란스 제중관\n" + _format_operating_hours(jejung),
        ]
    )

    values = {
        "last_updated": data.get("generated_at", "-"),
        "source_yonsei": "https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp",
        "source_aramark": "http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp",
        "summary_manna": _menu_count(manna),
        "summary_hankyung": _menu_count(eoulsam),
        "summary_jonghap": _menu_count(jonghap),
        "summary_jejung": _menu_count(jejung),
        "operating_hours_section": operating_hours_section,
        "day_quick_links": day_quick_links,
        "day_view_sections": "\n\n".join(day_sections),
        "table_manna": _build_week_table(
            manna.get("week", {}), _format_yonsei_entries, week_labels
        )
        if manna
        else _fallback_table("연세대학교 맛나샘 데이터가 없습니다."),
        "table_hankyung": _build_week_table(
            eoulsam.get("week", {}), _format_yonsei_entries, week_labels
        )
        if eoulsam
        else _fallback_table("연세대학교 한경관(어울샘) 데이터가 없습니다."),
        "table_jonghap": _build_week_table(
            jonghap.get("week", {}), _format_aramark_entries, week_labels
        )
        if jonghap
        else _fallback_table("세브란스 종합관 데이터가 없습니다."),
        "table_jejung": _build_week_table(
            jejung.get("week", {}), _format_aramark_entries, week_labels
        )
        if jejung
        else _fallback_table("세브란스 제중관 데이터가 없습니다."),
    }

    return template.format(**values)
