import asyncio

from .abstractions import IExerciseRepository, ISetRepository, IUserRepository, IWorkoutRepository

class Context:
    exercise_repository: IExerciseRepository = None
    set_repository: ISetRepository = None
    user_repository: IUserRepository = None
    workout_repository: IWorkoutRepository = None

    def save(self) -> None:
        self.exercise_repository.save()
        self.set_repository.save()
        self.user_repository.save()
        self.workout_repository.save()

    async def save_async(self) -> None:
        awaitables = [
            self.exercise_repository.save_async(),
            self.set_repository.save_async(),
            self.user_repository.save_async(),
            self.workout_repository.save_async()
        ]
        await asyncio.gather(*awaitables)