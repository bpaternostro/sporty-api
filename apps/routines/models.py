from django.db import models
from django.conf import settings

from ..main.models import SportyBaseModel, SportyBaseRelationsModel, SportyBaseRelationsLangModel


class Day(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="DayLang", blank=True)


class Goal(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="GoalLang", blank=True)
    image = models.ImageField(upload_to="routines/goals/images", blank=True)


class System(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="SystemLang", blank=True)
    image = models.ImageField(upload_to="routines/systems/images", blank=True)


class Cadence(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="CadenceLang", blank=True)


class Restriction(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="RestrictionLang", blank=True)
    image = models.ImageField(upload_to="routines/restrictions/images", blank=True)


class TrainingMethod(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="TrainingMethodLang", blank=True)
    image = models.ImageField(upload_to="routines/training-method/images", blank=True)


class ContactType(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="ContactTypeLang", blank=True)
    

class Level(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="LevelLang", blank=True)
    image = models.ImageField(upload_to="routines/levels/images", blank=True)


class RoutineType(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="RoutineTypeLang", blank=True)
    image = models.ImageField(upload_to="routines/routine-type/images", blank=True)


class Training(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="TrainingLang", blank=True)
    image = models.ImageField(upload_to="routines/training/images", blank=True)


class RoutineStatus(SportyBaseModel):
    class Meta:
        verbose_name = "Routine status"
        verbose_name_plural = "Routine status"
    lang = models.ManyToManyField("main.Language", through="RoutineStatusLang", blank=True)



class ExerciseStatus(SportyBaseModel):
    class Meta:
        verbose_name = "Exercise status"
        verbose_name_plural = "Exercise status"
    lang = models.ManyToManyField("main.Language", through="ExerciseStatusLang", blank=True)


class RoutineCustomerStatus(SportyBaseModel):
    class Meta:
        verbose_name = "Routine Customer status"
        verbose_name_plural = "Routine Customer status"
    
    lang = models.ManyToManyField("main.Language", through="RoutineCustomerStatusLang", blank=True)


class BlockStatus(SportyBaseModel):
    class Meta:
        verbose_name = "Block status"
        verbose_name_plural = "Block status"

    lang = models.ManyToManyField("main.Language", through="BlockStatusLang", blank=True)


class MuscleGroupType(SportyBaseModel):
    image = models.ImageField(upload_to="routines/muscle_group_type/images")
    lang = models.ManyToManyField("main.Language", through="MuscleGroupTypeLang", blank=True)


class MuscleGroup(SportyBaseModel):
    muscle_group_type = models.ForeignKey(MuscleGroupType, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="routines/muscle_group/images")
    lang = models.ManyToManyField("main.Language", through="MuscleGroupLang", blank=True)


class BlockType(SportyBaseModel):
    lang = models.ManyToManyField("main.Language", through="BlockTypeLang", blank=True)
    image = models.ImageField(upload_to="routines/blocks/images", blank=True)



class RoutineCustomers(SportyBaseRelationsModel):
    customer = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    routine = models.ForeignKey('Routine', on_delete=models.DO_NOTHING)
    status = models.ForeignKey(RoutineCustomerStatus, on_delete=models.DO_NOTHING)
    observation = models.TextField()
    start_date = models.DateField(blank=True)
    due_date = models.DateField(blank=True)

    class Meta:
        verbose_name = "Routine customers"
        verbose_name_plural = "Routine customers"


class ExerciseType(SportyBaseModel):
    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    lang = models.ManyToManyField("main.Language", through="ExerciseTypeLang", blank=True)


class Exercise(SportyBaseModel):
    description = models.TextField()
    type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(ExerciseStatus, on_delete=models.DO_NOTHING)
    video_link = models.URLField(blank=True)
    creator = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    muscle_group = models.ManyToManyField(MuscleGroup)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="routines/exercises/images")
    lang = models.ManyToManyField("main.Language", through="ExerciseLang", blank=True)


class Block(SportyBaseModel):
    status = models.ForeignKey(BlockStatus, on_delete=models.DO_NOTHING)
    creator = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    exercises = models.ManyToManyField(Exercise, through='BlockExerciseDetail')
    type = models.ForeignKey(BlockType, on_delete=models.DO_NOTHING)
    lang = models.ManyToManyField("main.Language", through="BlockLang", blank=True)


class BlockExerciseDetail(SportyBaseRelationsModel):
    block = models.ForeignKey(Block, on_delete=models.DO_NOTHING, default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    serie = models.IntegerField()
    reps = models.IntegerField()
    weight = models.CharField(max_length=10)
    pause = models.CharField(max_length=10)
    observation = models.TextField()


class Routine(SportyBaseModel):
    status = models.ForeignKey(RoutineStatus, on_delete=models.DO_NOTHING, default=1)
    description = models.TextField()
    routine_type = models.ForeignKey(RoutineType, on_delete=models.DO_NOTHING)
    restrictions = models.ManyToManyField(Restriction, blank=True)
    creator = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
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
    training_method = models.ForeignKey(TrainingMethod, on_delete=models.DO_NOTHING, blank=True)
    lang = models.ForeignKey("main.Language", on_delete=models.DO_NOTHING, default=1)


class RoutineDaysBlocks(SportyBaseRelationsModel):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING)
    blocks = models.ManyToManyField(Block)


class DayLang(SportyBaseRelationsLangModel):
    day = models.ForeignKey(Day, on_delete=models.DO_NOTHING)


class GoalLang(SportyBaseRelationsLangModel):
    goal = models.ForeignKey(Goal, on_delete=models.DO_NOTHING)


class SystemLang(SportyBaseRelationsLangModel):
    system = models.ForeignKey(System, on_delete=models.DO_NOTHING)


class CadenceLang(SportyBaseRelationsLangModel):
    candence = models.ForeignKey(Cadence, on_delete=models.DO_NOTHING)


class RestrictionLang(SportyBaseRelationsLangModel):
    restriction = models.ForeignKey(Restriction, on_delete=models.DO_NOTHING)


class TrainingMethodLang(SportyBaseRelationsLangModel):
    training_method = models.ForeignKey(TrainingMethod, on_delete=models.DO_NOTHING)


class ContactTypeLang(SportyBaseRelationsLangModel):
    contact_type = models.ForeignKey(ContactType, on_delete=models.DO_NOTHING)


class LevelLang(SportyBaseRelationsLangModel):
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)

class RoutineTypeLang(SportyBaseRelationsLangModel):
    routine_type = models.ForeignKey(RoutineType, on_delete=models.DO_NOTHING)


class TrainingLang(SportyBaseRelationsLangModel):
    training = models.ForeignKey(Training, on_delete=models.DO_NOTHING)


class RoutineStatusLang(SportyBaseRelationsLangModel):
    routine_status = models.ForeignKey(RoutineStatus, on_delete=models.DO_NOTHING)


class ExerciseStatusLang(SportyBaseRelationsLangModel):
    exercise_status = models.ForeignKey(ExerciseStatus, on_delete=models.DO_NOTHING)


class RoutineCustomerStatusLang(SportyBaseRelationsLangModel):
    routine_customer_status = models.ForeignKey(RoutineCustomerStatus, on_delete=models.DO_NOTHING)



class BlockStatusLang(SportyBaseRelationsLangModel):
    block_status = models.ForeignKey(BlockStatus, on_delete=models.DO_NOTHING)


class MuscleGroupTypeLang(SportyBaseRelationsLangModel):
    muscle_group_type = models.ForeignKey(MuscleGroupType, on_delete=models.DO_NOTHING)


class MuscleGroupLang(SportyBaseRelationsLangModel):
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.DO_NOTHING, default=0)


class ExerciseTypeLang(SportyBaseRelationsLangModel):
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING)


class ExerciseLang(SportyBaseRelationsLangModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)


class BlockLang(SportyBaseRelationsLangModel):
    block = models.ForeignKey(Block, on_delete=models.DO_NOTHING)


class BlockTypeLang(SportyBaseRelationsLangModel):
    block_type = models.ForeignKey(BlockType, on_delete=models.DO_NOTHING)
