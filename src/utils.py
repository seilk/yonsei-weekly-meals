from __future__ import annotations

from datetime import datetime, timedelta
from html import unescape
from typing import Iterable
import re
from zoneinfo import ZoneInfo

DAY_ORDER = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
DAY_LABELS_KO = {
    "mon": "월",
    "tue": "화",
    "wed": "수",
    "thu": "목",
    "fri": "금",
    "sat": "토",
    "sun": "일",
}
DAY_FROM_KO = {
    "월": "mon",
    "화": "tue",
    "수": "wed",
    "목": "thu",
    "금": "fri",
    "토": "sat",
    "일": "sun",
}


def kst_now_iso() -> str:
    return datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")


def normalize_space(text: str) -> str:
    text = unescape(text)
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_multiline_text(text: str) -> str:
    text = unescape(text)
    text = text.replace("\xa0", " ")
    text = text.replace("\r", "")
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.split("\n")]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def join_non_empty(values: Iterable[str], sep: str = ", ") -> str:
    return sep.join([v for v in values if v])


def init_week_map() -> dict[str, list[dict]]:
    return {day: [] for day in DAY_ORDER}


def build_week_labels_from_kst_now() -> dict[str, str]:
    now_kst = datetime.now(ZoneInfo("Asia/Seoul")).date()
    monday = now_kst - timedelta(days=now_kst.weekday())

    labels: dict[str, str] = {}
    for idx, day_key in enumerate(DAY_ORDER):
        day_date = monday + timedelta(days=idx)
        labels[day_key] = f"{DAY_LABELS_KO[day_key]}({day_date.strftime('%m/%d')})"
    return labels
