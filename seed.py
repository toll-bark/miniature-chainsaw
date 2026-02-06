import asyncio

from datetime import date

from miniaturechainsaw.io import Context
from miniaturechainsaw.schema.exercise import CreateExerciseSchema
from miniaturechainsaw.schema.set import CreateSetSchema
from miniaturechainsaw.schema.user import CreateUserSchema
from miniaturechainsaw.schema.workout import CreateWorkoutSchema

ctx: Context = Context()

# TODO: Initialize repositories

exercise_names = []
exercise_names.append("Barbell Incline Bench Press")
exercise_names.append("Dumbbell Shoulder Press")
exercise_names.append("Dumbbell Neutral Bicep Curl")
exercise_names.append("Barbell Back Squat")
exercise_names.append("Deadlift")
exercise_names.append("Barbell Back Row")
exercise_names.append("Elbow Plank")

for exercise_name in exercise_names:
    exercise_dto: CreateExerciseSchema = CreateExerciseSchema()
    exercise_dto.name = exercise_name
    ctx.exercise_repository.create_exercise(exercise_dto)

user_dto: CreateUserSchema = CreateUserSchema()
user_dto.name = "test user"
user_id: int = ctx.user_repository.create_user(user_dto)

upper_workout_dto: CreateWorkoutSchema = CreateWorkoutSchema()
upper_workout_dto.user_id = user_id
upper_workout_dto.scheduled_date = date(2027, 2, 4)
upper_workout_id: int = ctx.workout_repository.create_workout(upper_workout_dto)

lower_workout_dto: CreateWorkoutSchema = CreateWorkoutSchema()
lower_workout_dto.user_id = user_id
lower_workout_dto.scheduled_date = date(2027, 2, 5)
lower_workout_id: int = ctx.workout_repository.create_workout(lower_workout_dto)

sets: list[CreateSetSchema] = []

bench_set_dto: CreateSetSchema = CreateSetSchema()
bench_set_dto.workout_id = upper_workout_id
bench_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("barbell incline bench")[0]
bench_set_dto.weight = 150.
bench_set_dto.target_repetitions = 7
bench_set_dto.repetitions_metadata = None
sets.append(bench_set_dto)

shoulder_press_set_dto: CreateSetSchema = CreateSetSchema()
shoulder_press_set_dto.workout_id = upper_workout_id
shoulder_press_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("dumbbell shoulder press")[0]
shoulder_press_set_dto.weight = 135.
shoulder_press_set_dto.target_repetitions = 6
shoulder_press_set_dto.repetitions_metadata = None
sets.append(shoulder_press_set_dto)

curls_set_dto: CreateSetSchema = CreateSetSchema()
curls_set_dto.workout_id = upper_workout_id
curls_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("bicep curl")[0]
curls_set_dto.weight = 60.
curls_set_dto.target_repetitions = 8
curls_set_dto.repetitions_metadata = None
sets.append(curls_set_dto)

for i in range(0, len(sets)):
    set_dto = sets[i]
    for j in range(0, 3):
        set_dto.set_order = 4 * i + j
        ctx.set_repository.create_set(set_dto)
    set_dto.set_order = 4 * i + 3
    set_dto.target_repetitions = None
    ctx.set_repository.create_set(set_dto)

sets: list[CreateSetSchema] = []

squat_set_dto: CreateSetSchema = CreateSetSchema()
squat_set_dto.workout_id = lower_workout_id
squat_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("back squat")[0]
squat_set_dto.weight = 225.
squat_set_dto.target_repetitions = 8
squat_set_dto.repetitions_metadata = None
sets.append(squat_set_dto)

row_set_dto: CreateSetSchema = CreateSetSchema()
row_set_dto.workout_id = lower_workout_id
row_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("back row")[0]
row_set_dto.weight = 185.
row_set_dto.target_repetitions = 5
row_set_dto.repetitions_metadata = None
sets.append(row_set_dto)

plank_set_dto: CreateSetSchema = CreateSetSchema()
plank_set_dto.workout_id = lower_workout_id
plank_set_dto.exercise_id = ctx.exercise_repository.read_exercises_containing_name("plank")[0]
plank_set_dto.weight = 0.
plank_set_dto.target_repetitions = 105
plank_set_dto.repetitions_metadata = "seconds"
sets.append(plank_set_dto)

for i in range(0, len(sets)):
    set_dto = sets[i]
    for j in range(0, 3):
        set_dto.set_order = 4 * i + j
        ctx.set_repository.create_set(set_dto)
    set_dto.set_order = 4 * i + 3
    set_dto.target_repetitions = None
    ctx.set_repository.create_set(set_dto)

asyncio.run(ctx.save_async())