from __future__ import annotations

import json
import re
from collections import OrderedDict

import requests
from bs4 import BeautifulSoup

from src.utils import (
    DAY_ORDER,
    build_retry_session,
    clean_multiline_text,
    init_week_map,
    normalize_space,
)

YONSEI_URL = "https://www.yonsei.ac.kr/_custom/yonsei/m/menu.jsp"


def fetch_yonsei_html(
    timeout: int = 30, session: requests.Session | None = None
) -> str:
    sess = session or build_retry_session()
    resp = sess.get(YONSEI_URL, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def extract_week_data_json(html: str) -> list:
    match = re.search(r"var\s+weekData\s*=\s*(\[[\s\S]*?\]);", html)
    if not match:
        raise ValueError("weekData variable not found in Yonsei page")
    raw = match.group(1)
    raw = re.sub(r",\s*([}\]])", r"\1", raw)
    return json.loads(raw)


def html_to_text(value: str) -> str:
    soup = BeautifulSoup(value or "", "html.parser")
    return clean_multiline_text(soup.get_text("\n"))


def parse_yonsei_week_data(week_data: list) -> list[dict]:
    restaurants: OrderedDict[tuple[str, str], dict] = OrderedDict()

    for day_index, campuses in enumerate(week_data):
        if day_index >= len(DAY_ORDER):
            break
        day_key = DAY_ORDER[day_index]
        for campus_entry in campuses or []:
            campus_name = normalize_space(campus_entry.get("campusName", ""))
            for refectory in campus_entry.get("refectory", []) or []:
                name = normalize_space(refectory.get("name", ""))
                key = (campus_name, name)
                if key not in restaurants:
                    restaurants[key] = {
                        "name": name,
                        "campus": campus_name,
                        "group": "yonsei_university",
                        "operating_hours": html_to_text(refectory.get("time", "")),
                        "notes": html_to_text(refectory.get("info", "")),
                        "week": init_week_map(),
                    }

                sections: list[dict] = []
                for menu_type in refectory.get("type", []) or []:
                    category = normalize_space(menu_type.get("name", ""))
                    items = []
                    for item in menu_type.get("item", []) or []:
                        item_name = normalize_space(item.get("name", ""))
                        item_price = normalize_space(str(item.get("price", "")))
                        if item_name:
                            items.append(
                                {
                                    "name": item_name,
                                    "price": item_price,
                                    "time_code": normalize_space(item.get("time", "")),
                                }
                            )
                    if category or items:
                        sections.append({"category": category, "items": items})

                restaurants[key]["week"][day_key] = sections

    return list(restaurants.values())


def parse_yonsei() -> list[dict]:
    session = build_retry_session()
    html = fetch_yonsei_html(session=session)
    week_data = extract_week_data_json(html)
    return parse_yonsei_week_data(week_data)
