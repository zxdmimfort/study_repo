import datetime
import json
from api import register_booking


class Booking:
    def __init__(self, name: str, start: datetime.datetime, end: datetime.datetime) -> None:
        if start > end:
            raise ValueError
        
        self.room_name = name
        self.start = start
        self.end = end
    

    def otday_json(self):
        return {
            "room_name": self.room_name,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "duration": self.duration,
        }


    @property
    def duration(self):
        return (self.end - self.start).total_seconds() // 60
    
    
    @property
    def start_date(self):
        return self.start.strftime("%Y-%m-%d")
    
    
    @property
    def end_date(self):
        return self.end.strftime("%Y-%m-%d")
    
    
    @property
    def start_time(self):
        return self.start.strftime("%H:%M")
    
    
    @property
    def end_time(self):
        return self.end.strftime("%H:%M")


def create_booking(room_name: str, start: datetime.datetime, end: datetime.datetime) -> str:
    print("Начинаем создание бронирования")
    booking = Booking(room_name, start, end)
    try:
        created = register_booking(booking)
        if created:
            msg = "Бронирование создано"
        else:
            msg = "Комната занята"
    except KeyError:
        created = False
        msg = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")
    return json.dumps(
        {
        "created": created,
        "msg": msg,
        "booking": booking.otday_json()
        }, ensure_ascii=False, indent=2)



result = create_booking("Вагнер", datetime.datetime(2022,9, 1, 14), datetime.datetime(2022,9,1,15,15))
print(result)

booking = Booking("Вагнер", datetime.datetime(2022,9, 1, 14), datetime.datetime(2022,9,1,15,15))
