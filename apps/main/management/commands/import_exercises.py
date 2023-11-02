from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _process_list, _get_data_from_gsheet, _get_or_create_obj
from ...constants import LanguagesChoices
from googletrans import Translator, constants


class Command(BaseCommand):
    help = "Imports the routines from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_exercises = (
            []
        )  # creates an auxiliar list to check if book is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM",
            sheet="exercises",
        )
        translator = Translator()
        contact_type = _get_or_create_obj(ContactType, name="phone")
        customer_type = _get_or_create_obj(CustomerType, name="trainer")

        creator = _get_or_create_obj(
            Customer, name="Bruno", username="bpaternostro", surname="Paternostro"
        )

        for _item in data:
            if (
                _item.get("name") not in self.list_of_exercises
            ):  # check if exercise is repeated
                training_method = _get_or_create_obj(
                    TrainingMethod, name=_item.get("training")
                )
                training = _get_or_create_obj(
                    Training,
                    name=_item.get("training")
                )
                tipo = _get_or_create_obj(
                    ExerciseType,
                    name=_item.get("tipo"),
                    creator=creator,
                    training=training,
                )
                level = _get_or_create_obj(Level, name=_item.get("level"))
                status = _get_or_create_obj(
                    ExerciseStatus, name=_item.get("status")
                )

                muscle_group = [
                    _get_or_create_obj(MuscleGroup, name=m)
                    for m in _item.get("muscle_group").split(",")
                ]

                muscle_group = [
                    _get_or_create_obj(MuscleGroup, name=m)
                    for m in _item.get("muscle_group").split(",")
                ]

                exercise = Exercise.objects.create(
                    name=_item.get("name"),
                    description=_item.get("description"),
                    type=tipo,
                    status=status,
                    creator=creator,
                    level=level,
                    video_link=_item.get("video_link"),
                    image="http://demo.com",
                )

                _process_list(
                    muscle_group, exercise.muscle_group
                )  # process muscle_group

                self.list_of_exercises.append(_item.get("name"))
                exercise.save()

                for l in LanguagesChoices.choices:
                    lang = l[0]
                    value_to_translate = _item.get("name")
                    traslation = translator.translate(value_to_translate, dest=lang, src="es")
                    exercise_lang = ExerciseLang.objects.create(
                        lang = _get_or_create_obj(Language, name=l[1].lower()),
                        translation = traslation.text.lower(),
                        exercise = _get_or_create_obj(Exercise, name=value_to_translate)
                    )
                    exercise_lang.save()
