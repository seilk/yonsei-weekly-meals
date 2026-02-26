from __future__ import annotations

import json
from pathlib import Path

from src.parsers.aramark import parse_aramark
from src.parsers.yonsei import parse_yonsei
from src.readme_generator import render_readme
from src.utils import kst_now_iso


def build_payload() -> dict:
    yonsei_restaurants = parse_yonsei()
    aramark_restaurants = parse_aramark()

    return {
        "generated_at": kst_now_iso(),
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
