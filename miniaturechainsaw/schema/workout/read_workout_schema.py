from datetime import date, datetime

class ReadWorkoutSchema:
    id: int
    user_id: int
    scheduled_date: date
    start_timestamp: datetime | None
    end_timestamp: datetime | None