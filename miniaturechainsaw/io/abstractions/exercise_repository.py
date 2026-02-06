from abc import ABC, abstractmethod

from . import IRepository
from ...schema.exercise import CreateExerciseSchema, ReadExerciseSchema

class IExerciseRepository(IRepository, ABC):
    @abstractmethod
    def create_exercise(self, dto: CreateExerciseSchema) -> int:
        pass

    @abstractmethod
    def read_exercise(self, id: int) -> ReadExerciseSchema:
        pass

    @abstractmethod
    def read_all_exercises(self) -> list[ReadExerciseSchema]:
        pass

    @abstractmethod
    def read_exercises_containing_name(self, substring: str) -> list[ReadExerciseSchema]:
        pass

    @abstractmethod
    def delete_exercise(self, id: int) -> None:
        pass