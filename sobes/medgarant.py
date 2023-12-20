from datetime import datetime, timedelta


def get_working_periods(
    working_time: dict[str, str],
    busy: list[dict[str, str]],
    interval: timedelta,
    format: str,
):
    res = []
    interval = timedelta(minutes=30)

    stop_busy = [datetime.strptime(working_time["begin"], format)] + sorted(
        [datetime.strptime(d["stop"], format) for d in busy]
    )
    start_busy = sorted([datetime.strptime(d["start"], format) for d in busy]) + [
        datetime.strptime(working_time["end"], format)
    ]

    for start, stop in zip(stop_busy, start_busy):
        duration = stop - (cur := start)
        for i in range(duration // interval):
            res.append((cur, (cur := cur + interval)))

    return [
        {"start": start.strftime(format), "stop": stop.strftime(format)}
        for start, stop in res
    ]


if __name__ == "__main__":
    busy = [
        {"start": "10:30", "stop": "10:50"},
        {"start": "18:40", "stop": "18:50"},
        {"start": "14:40", "stop": "15:50"},
        {"start": "16:40", "stop": "17:20"},
        {"start": "20:05", "stop": "20:20"},
    ]
    working_hours = {"begin": "9:00", "end": "21:00"}
    format = "%H:%M"
    interval = timedelta(minutes=30)
    working_periods = get_working_periods(working_hours, busy, interval, format)
    print(f"Всего получилось {len(working_periods)} окошек", *working_periods, sep="\n")
