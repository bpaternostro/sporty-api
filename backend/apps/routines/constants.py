from django.db import models


class RestrictionsChoices(models.IntegerChoices):
    MEDICAL_CONDITION = 1, ('Condiciones Medicas')
    INJURIES = 2, ('Lesiones')
    CHRONIC_ILLNESS = 3, ('Lesiones cronicas')
    NEUROLOGICAL_CONDITIONS = 4, ('Condiciones neurologicas')
    ORTHOPEDIC_CONCERNS = 5, ('Ortopedia')
    BALANCE_ISSUES = 6, ('Problemas de estabilidad')
    AGE_RELATED_FACTORS = 7, ('Factores relacionados con la edad')
    PREGNANCY = 8, ('Embarazos')
    MEDICATION_SIDE_EFFECTS = 9, ('Efectos secundarios por medicación')
    ALLERGIES = 10, ('Alergias')
    MENTAL_HEALTH_CONCERNS = 11, ('Enfermedades mentales')


class GoalsChoices(models.IntegerChoices):
    ACHIEVE_A_HEALTHY_WEIGHT= 1, ('Alcanzar un peso saludable')
    MUSCLE_BUILDING = 2, ('Construcción de musculo')
    STRENGTH_TRAINING = 3, ('Mejorar la fuerza')
    ENDURANCE = 4, ('Mejorar Resistencia')
    FLEXIBILITY = 5, ('Mejorar Flexibilidad')
    FUCTIONAL_FITNESS = 6, ('Mejorar fuerza/balance/coordinación')
    SPORT_SPECIFIC_TRAINING = 7, ('Mejorar entrenamiento especifico')
    CORE_STRENGTH = 8, ('Fortalecer el CORE')
    BALANCE_AND_COORDINATION = 9, ('Mejorar el balance y la coordinación')
    HEALTH_AND_WELL_BEING = 10, ('Salud y bienestar')
    INJURY_REHABILITATION = 11, ('Rehabilitación de lesion')


class TrainingMethodChoices(models.IntegerChoices):
    STRENGTH= 1, ('Fuerza')
    ENDURANCE = 2, ('Resistencia')
    SPEED = 3, ('Velocidad')
    FLEXIBILITY = 4, ('Flexibilidad')


class ContactTypeChoices(models.IntegerChoices):
    EMAIL= 1, ('Email')
    PHONE = 2, ('Phone')

class LevelChoices(models.IntegerChoices):
    INITIAL= 1, ('Inicial')
    MEDIUM = 2, ('Mediano')
    ADVANCE = 3, ('Avanzado')
    HIGH_PERFORMANCE = 4, ('Alto rendimiento')


class DayChoices(models.IntegerChoices):
    SUNDAY= 1, ('Domingo')
    MONDAY= 2, ('Lunes')
    TUESDAY= 3, ('Martes')
    WENDESDAY= 4, ('Miercoles')
    THURSDAY= 5, ('Jueves')
    FRIDAY= 6, ('Viernes')
    SATURDAY= 7, ('Sabado')


class CadenceChoices(models.IntegerChoices):
    CLASSIC= 1, ('Clasica 2-0-1')


class SystemChoices(models.IntegerChoices):
    PPLS= 1, ('Push Pull Legs Fuerza')
    PPLH= 2, ('Push Pull Legs Hipertrofia')
    FBS= 3, ('Full Body Strength')
    DRH= 4, ('Rutina dividida Hipertrofia')


class RoutineTypeChoices(models.IntegerChoices):
    WEEKLY= 1, ('semanal')
    BIWEEKLY= 2, ('quincenal')
    TRIWEEKLY= 3, ('trisemanal')
    MONTHLY= 4, ('Mensual')
    QUARTELY= 5, ('Trimestral')


class TrainingChoices(models.IntegerChoices):
    FUCNTIONAL= 1, ('Funcional')
    HIIT= 2, ('Hiit')
    CROSSFIT= 3, ('Crossfit')
    YOGA= 4, ('Yoga')
    RUNNING= 5, ('Running')


class StatusChoices(models.IntegerChoices):
    IN_PROGRESS= 1, ('En progreso')
    READY= 2, ('Lista')
    PAUSED= 3, ('Pausada')
    DONE= 4, ('Realizada')


class ExerciseTypeChoices(models.IntegerChoices):
    MOVILITY= 1, ('Movilidad')
    METABOLIC= 2, ('Metabolicos')
    LOP= 3, ('Lop')
    PLIOMETRIA= 4, ('Pliometria')
    COMPOUND= 5, ('Compuestos')
    STRECH= 6, ('Estiramiento')
    RELAX= 7, ('Relajacion')
    UPPER_BODY= 8, ('Tren superior')
    LOWER_BODY= 9, ('Tren inferior')
    CORE= 10, ('Zona media')

class RoutineCustomerStatusChoices(models.IntegerChoices):
    pass


class BlockStatusChoices(models.IntegerChoices):
    pass


class MuscleGroupTypeChoices(models.IntegerChoices):
    UPPER_BODY= 1, ('Tren superior')
    ARMS= 2, ('Brazos')
    LEGS= 3, ('Piernas')
    CORE= 4, ('Core')


class MuscleGroupChoices(models.IntegerChoices):
    LATISSINUS_DORSI= 1, ('Dorsal Ancho')
    PECS= 2, ('Pectorales')
    TRAPEZIUS= 3, ('Trapecios')
    BACK= 4, ('Espalda')
    ABS= 5, ('Abdominales')
    DELTOID= 6, ('Deltoides')
    BICEPS= 7, ('Bíceps')
    TRICEPS= 8, ('Triceps')
    FOREARMS= 9, ('Antebrazos')
    QUADRICEPS= 10, ('Quadríceps')
    FEMORAL_BICEPS= 11, ('Bíceps femorales')
    ADDUCTORS= 12, ('Aductores/Abductores')
    CALVES= 13, ('Gemelos')
    GLUTES= 14, ('Gluteos')
    HAMSTRING= 15, ('Izquiotibiales')


class BlockTypeChoices(models.IntegerChoices):
    WARM_UP= 13, ('Calentamiento')
    POST_TRAINING= 14, ('Post entrenamiento')
    TRAINING= 15, ('Entrenamiento')


class YesNoChoices(models.IntegerChoices):
    NO= 0, ('No')
    YES= 1, ('Si')
