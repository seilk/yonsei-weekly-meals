from __future__ import annotations

import json
from pathlib import Path

from src.parsers.aramark import parse_aramark
from src.parsers.yonsei import parse_yonsei
from src.readme_generator import render_readme
from src.utils import build_week_labels_from_kst_now, kst_now_iso, today_day_key_kst


def build_payload() -> dict:
    warnings: list[str] = []

    try:
        yonsei_restaurants = parse_yonsei()
    except Exception as exc:
        yonsei_restaurants = []
        warnings.append(f"Yonsei parser failed: {exc}")

    try:
        aramark_restaurants = parse_aramark()
    except Exception as exc:
        aramark_restaurants = []
        warnings.append(f"Aramark parser failed: {exc}")

    week_labels = build_week_labels_from_kst_now()
    today_key = today_day_key_kst()

    if not yonsei_restaurants:
        warnings.append("Yonsei data is empty.")
    if not aramark_restaurants:
        warnings.append("Aramark data is empty.")

    yonsei_names = {r.get("name", "") for r in yonsei_restaurants}
    aramark_names = {r.get("name", "") for r in aramark_restaurants}

    for required in ["맛나샘", "어울샘(한경관)"]:
        if required not in yonsei_names:
            warnings.append(f"Yonsei expected restaurant missing: {required}")

    for required in ["종합관", "제중관"]:
        if required not in aramark_names:
            warnings.append(f"Aramark expected restaurant missing: {required}")

    return {
        "generated_at": kst_now_iso(),
        "week_labels": week_labels,
        "today_key": today_key,
        "today_label": week_labels.get(today_key, today_key),
        "warnings": warnings,
        "sources": [
            {
                "name": "yonsei_weekly_menu",
                "url": "https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp",
            },
            {
                "name": "severance_aramark_mobile",
                "url": "http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp",
            },
        ],
        "yonsei_university": {"restaurants": yonsei_restaurants},
        "severance_aramark": {"restaurants": aramark_restaurants},
    }


def write_outputs(project_root: Path, payload: dict) -> None:
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    weekly_json = data_dir / "weekly.json"
    weekly_json.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    template_path = project_root / "templates" / "README.template.md"
    readme = render_readme(payload, template_path=template_path)
    (project_root / "README.md").write_text(readme, encoding="utf-8")


def update(project_root: Path | None = None) -> dict:
    root = (project_root or Path(__file__).resolve().parent.parent).resolve()
    payload = build_payload()
    write_outputs(root, payload)
    return payload
