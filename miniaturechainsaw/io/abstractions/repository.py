from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def save(self) -> None:
        pass

    @abstractmethod
    async def save_async(self) -> None:
        pass