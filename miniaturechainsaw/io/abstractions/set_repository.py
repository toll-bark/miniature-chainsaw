from abc import ABC, abstractmethod

from . import IRepository
from ...schema.set import CreateSetSchema, ReadSetSchema, UpdateSetSchema

class ISetRepository(IRepository, ABC):
    @abstractmethod
    def create_set(self, dto: CreateSetSchema) -> int:
        pass

    @abstractmethod
    def read_set(self, id: int) -> ReadSetSchema:
        pass

    @abstractmethod
    def read_sets_by_user(self, user_id: int) -> list[ReadSetSchema]:
        pass

    @abstractmethod
    def read_sets_by_workout(self, workout_id: int) -> list[ReadSetSchema]:
        pass

    @abstractmethod
    def update_set(self, id: int, dto: UpdateSetSchema) -> None:
        pass

    @abstractmethod
    def delete_set(self, id: int) -> None:
        pass