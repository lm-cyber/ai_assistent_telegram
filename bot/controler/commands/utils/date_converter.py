from datetime import datetime
from timefhuman import timefhuman


def date_convect(date_str: str):
    try:
        return timefhuman(date_str, now=datetime.now())
    except Exception:
        return None
