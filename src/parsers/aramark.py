from __future__ import annotations

from collections import OrderedDict
import re

import requests
from bs4 import BeautifulSoup

from src.utils import DAY_FROM_KO, build_retry_session, init_week_map, normalize_space

BASE_URL = "http://m.yonsei.aramark.co.kr/mobile/yonsei/index.jsp"
MEAL_TIME_MAP = {"m": "조식", "a": "중식", "e": "석식"}
RESTAURANT_MAP = {
    1: "종합관",
    2: "제중관",
    3: "교수식당",
    4: "ABMRC",
}


def day_key_from_label(label: str) -> str | None:
    label = normalize_space(label)
    match = re.search(r"([월화수목금토일])", label)
    if not match:
        return None
    return DAY_FROM_KO.get(match.group(1))


def fetch_aramark_html(
    meal_time: str,
    fz_no: int,
    timeout: int = 30,
    session: requests.Session | None = None,
) -> str:
    sess = session or build_retry_session()
    resp = sess.get(
        BASE_URL,
        params={"meal_time": meal_time, "fz_no": str(fz_no)},
        timeout=timeout,
    )
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or resp.encoding
    return resp.text


def parse_aramark_html(html: str, meal_time: str) -> dict[str, list[dict]]:
    soup = BeautifulSoup(html, "html.parser")
    week_map = init_week_map()

    for section in soup.select("div.section1"):
        for li in section.select("li.list"):
            dt = li.find("dt")
            dd = li.find("dd")
            if not dt or not dd:
                continue

            span = dt.find("span")
            day_label = normalize_space(span.get_text(" ", strip=True) if span else "")
            day_key = day_key_from_label(day_label)
            if not day_key:
                continue

            span_text = normalize_space(span.get_text(" ", strip=True) if span else "")
            full_title = normalize_space(dt.get_text(" ", strip=True))
            category = normalize_space(full_title.replace(span_text, "").strip())

            items = [normalize_space(x) for x in dd.stripped_strings]
            items = [x for x in items if x]
            if not items and not category:
                continue

            week_map[day_key].append(
                {
                    "meal_time": MEAL_TIME_MAP.get(meal_time, meal_time),
                    "category": category,
                    "items": items,
                }
            )

    return week_map


def parse_aramark() -> list[dict]:
    restaurants: OrderedDict[int, dict] = OrderedDict()

    for fz_no, restaurant_name in RESTAURANT_MAP.items():
        restaurants[fz_no] = {
            "name": restaurant_name,
            "campus": "세브란스",
            "group": "severance_aramark",
            "operating_hours": "",
            "notes": "",
            "week": init_week_map(),
        }

    session = build_retry_session()
    for fz_no in RESTAURANT_MAP:
        for meal_time in MEAL_TIME_MAP:
            html = fetch_aramark_html(
                meal_time=meal_time,
                fz_no=fz_no,
                session=session,
            )
            parsed = parse_aramark_html(html, meal_time=meal_time)
            for day_key, entries in parsed.items():
                restaurants[fz_no]["week"][day_key].extend(entries)

    return list(restaurants.values())
