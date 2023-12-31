from datetime import datetime, timedelta


def time_delta(t1, t2) -> str:
    date_time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date_time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    time_diff = date_time2 - date_time1 if date_time2 > date_time1 else date_time1 - date_time2

    return str(int(time_diff.total_seconds()))

