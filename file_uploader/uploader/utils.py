from datetime import datetime, timezone


def is_the_past(date):
    return date <= datetime.now(tz=timezone.utc)
