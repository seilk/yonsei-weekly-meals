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
            lines.append(
                f"{category}: {', '.join(items)}" if category else ", ".join(items)
            )
    return "<br>".join(lines) if lines else "데이터 없음"


def _format_aramark_entries(entries: list[dict]) -> str:
    lines: list[str] = []
    for entry in entries:
        meal = entry.get("meal_time", "")
        category = entry.get("category", "")
        items = entry.get("items", [])
        menu = ", ".join(items) if items else "데이터 없음"
        prefix = join_non_empty([meal, category], " ")
        lines.append(f"[{prefix}] {menu}" if prefix else menu)
    return "<br>".join(lines) if lines else "데이터 없음"


def _build_week_table(week: dict[str, list[dict]], formatter) -> str:
    lines = ["| 요일 | 메뉴 |", "|---|---|"]
    for day_key in DAY_ORDER:
        day_label = DAY_LABELS_KO[day_key]
        value = formatter(week.get(day_key, []))
        lines.append(f"| {day_label} | {value} |")
    return "\n".join(lines)


def _find_restaurant(restaurants: list[dict], target_name: str) -> dict | None:
    for r in restaurants:
        if r.get("name") == target_name:
            return r
    return None


def _fallback_table(message: str) -> str:
    return "\n".join(["| 요일 | 메뉴 |", "|---|---|", f"| - | {message} |"])


def render_readme(data: dict, template_path: Path) -> str:
    template = template_path.read_text(encoding="utf-8")

    yonsei_restaurants = data.get("yonsei_university", {}).get("restaurants", [])
    aramark_restaurants = data.get("severance_aramark", {}).get("restaurants", [])

    manna = _find_restaurant(yonsei_restaurants, "맛나샘")
    eoulsam = _find_restaurant(yonsei_restaurants, "어울샘(한경관)")
    jonghap = _find_restaurant(aramark_restaurants, "종합관")
    jejung = _find_restaurant(aramark_restaurants, "제중관")

    values = {
        "last_updated": data.get("generated_at", "-"),
        "source_yonsei": "https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp",
        "source_aramark": "http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp",
        "table_manna": _build_week_table(manna.get("week", {}), _format_yonsei_entries)
        if manna
        else _fallback_table("연세대학교 맛나샘 데이터가 없습니다."),
        "table_hankyung": _build_week_table(
            eoulsam.get("week", {}), _format_yonsei_entries
        )
        if eoulsam
        else _fallback_table("연세대학교 한경관(어울샘) 데이터가 없습니다."),
        "table_jonghap": _build_week_table(
            jonghap.get("week", {}), _format_aramark_entries
        )
        if jonghap
        else _fallback_table("세브란스 종합관 데이터가 없습니다."),
        "table_jejung": _build_week_table(
            jejung.get("week", {}), _format_aramark_entries
        )
        if jejung
        else _fallback_table("세브란스 제중관 데이터가 없습니다."),
    }

    return template.format(**values)
