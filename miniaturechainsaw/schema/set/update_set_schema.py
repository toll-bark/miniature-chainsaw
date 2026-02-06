from datetime import datetime

class UpdateSetSchema:
    weight: float | None
    target_repetitions: int | None
    repetitions: int
    timestamp: datetime | None
    completed: bool