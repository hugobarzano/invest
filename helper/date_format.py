from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def date_parse(date):
    return datetime.strptime(date, DATE_FORMAT)


def date_iso(date):
    return date_parse(date).isoformat()
