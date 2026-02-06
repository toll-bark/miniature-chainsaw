from datetime import date, datetime

class Workout:
    id: int
    user_id: int
    scheduled_date: date
    start_timestamp: datetime | None
    end_timestamp: datetime | None