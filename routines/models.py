from django.db import models


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class StatusType(BaseModel):
    name = models.CharField(max_length=50)


class Day(BaseModel):
    name = models.CharField(max_length=50)


class Status(BaseModel):
    name = models.CharField(max_length=50)
    status_type = models.ForeignKey(StatusType, on_delete=models.DO_NOTHING)


class Goal(BaseModel):
    name = models.CharField(max_length=50)


class System(BaseModel):
    name = models.CharField(max_length=50)


class Cadence(BaseModel):
    name = models.CharField(max_length=50)


class Restriction(BaseModel):
    name = models.CharField(max_length=50)


class TrainingMethod(BaseModel):
    name = models.CharField(max_length=50)


class Training(BaseModel):
    name = models.CharField(max_length=50)
    training_method = models.ForeignKey(TrainingMethod, on_delete=models.DO_NOTHING)
    description = models.TextField()


class ContactType(BaseModel):
    name = models.CharField(max_length=50)


class Level(BaseModel):
    name = models.CharField(max_length=50)


class MuscleGroupType(BaseModel):
    name = models.CharField(max_length=50)
    image = models.TextField()


class MuscleGroup(BaseModel):
    name = models.CharField(max_length=200)
    muscle_group_type = models.ForeignKey(MuscleGroupType, on_delete=models.DO_NOTHING)
    image = models.TextField()


class CustomerType(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Customer(BaseModel):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    contact_type = models.ForeignKey(ContactType, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.DO_NOTHING)


class RoutineType(BaseModel):
    name = models.CharField(max_length=200)


class ExerciseType(BaseModel):
    name = models.CharField(max_length=200)
    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)


class Exercise(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    video_link = models.TextField()
    creator = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    muscle_group = models.ManyToManyField(MuscleGroup)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    image = models.TextField()


class Block(BaseModel):
    name = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    exercises = models.ManyToManyField(Exercise, through="BlockExercise", blank=True)


class BlockExercise(BaseModel):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    serie = models.IntegerField()
    reps = models.IntegerField()
    weight = models.CharField(max_length=50)
    pause = models.CharField(max_length=50)
    observation = models.TextField()


class Routine(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    routine_type = models.ForeignKey(RoutineType, on_delete=models.DO_NOTHING)
    restrictions = models.ManyToManyField(Restriction, blank=True)
    creator = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    system = models.ForeignKey(System, on_delete=models.DO_NOTHING)
    cadence = models.ForeignKey(Cadence, on_delete=models.DO_NOTHING)
    warm_up = models.CharField(max_length=50)
    cardio = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    pre_exhaustion = models.CharField(max_length=50)
    activation = models.CharField(max_length=50)
    rest_between_exercises = models.CharField(max_length=50)
    days_of_week = models.ManyToManyField(Day, through="RoutineDaysBlocks", blank=True)
    goals = models.ManyToManyField(Goal)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)


class RoutineDaysBlocks(BaseModel):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING)
    blocks = models.ManyToManyField(Block)
