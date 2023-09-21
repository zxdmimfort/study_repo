from dataclasses import dataclass
from typing import Literal

@dataclass(order=True, frozen=True)
class Event:
    day: int
    hour: int
    minute: int
    id: int
    status: Literal["A", "B", "S", "C"]
    
    def time_stamp(self):
        return self.minute + 60 * (self.hour + 24 * self.day)
    
    

events = [
    Event(*[
        int(value) if i < 4 else str(value)
        for i, value in enumerate(input().split())])
    for _ in range(int(input()))
    ]


rockets_events = {}

for event in events:
    rockets_events[event.id] = rockets_events.get(event.id, []) + [event]

for rocket in rockets_events.values():
    rocket.sort()


def rocket_flight_time(rocket_events: list[Event]):
    flight_time = 0
    last_start = None
    for event in rocket_events:
        if last_start is None and event.status == "A":
            last_start = event
            continue
        if last_start is not None and event.status in ["C", "S"]:
            flight_time += event.time_stamp() - last_start.time_stamp()
            last_start = None
    
    return flight_time


res = []
for rocket in sorted(list(rockets_events.keys())):
    res.append(rocket_flight_time(rockets_events[rocket]))
print(' '.join([str(num) for num in res]))
