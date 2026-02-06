from datetime import datetime

class ReadSetSchema:
    id: int
    workout_id: int
    exercise_id: int
    set_order: int
    weight: float | None
    target_repetitions: int | None
    repetitions: int | None
    repetitions_metadata: str | None
    timestamp: datetime | None
    completed: bool