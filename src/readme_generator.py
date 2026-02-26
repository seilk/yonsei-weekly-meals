from __future__ import annotations

from pathlib import Path

from src.utils import DAY_LABELS_KO, DAY_ORDER, join_non_empty


def _format_yonsei_entries(entries: list[dict]) -> str:
    lines: list[str] = []
    for section in entries:
        category = section.get("category", "")
        items = [
            i.get("name", "") for i in section.get("items", []) if i.get("name", "")
        ]
        if items:
            title = f"**{category}**" if category else "**메뉴**"
            lines.append(f"{title}: {', '.join(items)}")
    return "<br>".join(lines) if lines else "-"


def _format_aramark_entries(entries: list[dict]) -> str:
    lines: list[str] = []
    for entry in entries:
        meal = entry.get("meal_time", "")
        category = entry.get("category", "")
        items = entry.get("items", [])
        menu = ", ".join(items) if items else "-"
        prefix = join_non_empty([meal, category], " · ")
        lines.append(f"**{prefix}**: {menu}" if prefix else menu)
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


def render_readme(data: dict, template_path: Path) -> str:
    template = template_path.read_text(encoding="utf-8")

    yonsei_restaurants = data.get("yonsei_university", {}).get("restaurants", [])
    aramark_restaurants = data.get("severance_aramark", {}).get("restaurants", [])
    week_labels = data.get("week_labels", {})

    manna = _find_restaurant(yonsei_restaurants, "맛나샘")
    eoulsam = _find_restaurant(yonsei_restaurants, "어울샘(한경관)")
    jonghap = _find_restaurant(aramark_restaurants, "종합관")
    jejung = _find_restaurant(aramark_restaurants, "제중관")

    values = {
        "last_updated": data.get("generated_at", "-"),
        "source_yonsei": "https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp",
        "source_aramark": "http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp",
        "summary_manna": _menu_count(manna),
        "summary_hankyung": _menu_count(eoulsam),
        "summary_jonghap": _menu_count(jonghap),
        "summary_jejung": _menu_count(jejung),
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
