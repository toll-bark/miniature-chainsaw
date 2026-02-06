from abc import ABC, abstractmethod

from . import IRepository
from ...schema.workout import CreateWorkoutSchema, ReadWorkoutSchema, UpdateWorkoutSchema

class IWorkoutRepository(IRepository, ABC):
    @abstractmethod
    def create_workout(self, dto: CreateWorkoutSchema) -> int:
        pass

    @abstractmethod
    def read_workout(self, id: int) -> ReadWorkoutSchema:
        pass

    @abstractmethod
    def read_workouts_by_user_id(self, user_id: int) -> list[ReadWorkoutSchema]:
        pass

    @abstractmethod
    def update_workout(self, id: int, dto: UpdateWorkoutSchema) -> None:
        pass

    @abstractmethod
    def delete_workout(self, id: int) -> None:
        pass