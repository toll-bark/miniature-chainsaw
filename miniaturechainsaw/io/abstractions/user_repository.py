from abc import ABC, abstractmethod

from . import IRepository
from ...schema.user import CreateUserSchema, ReadUserSchema, UpdateUserSchema

class IUserRepository(IRepository, ABC):
    @abstractmethod
    def create_user(self, dto: CreateUserSchema) -> int:
        pass

    @abstractmethod
    def read_user(self, id: int) -> ReadUserSchema:
        pass

    @abstractmethod
    def update_user(self, id: int, dto: UpdateUserSchema) -> None:
        pass

    @abstractmethod
    def delete_user(self, id: int) -> None:
        pass