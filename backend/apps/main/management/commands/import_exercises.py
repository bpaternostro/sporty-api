import os
from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _process_list, _get_data_from_gsheet, _get_or_create_obj, _get_choice_id, _get_or_create_user
from ...constants import LanguagesChoices
from ....routines.constants import *

class Command(BaseCommand):
    help = "Imports the exercises from a dataset"

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
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="exercises",
        )

        creator = _get_or_create_user(
            CustomUser, email="bruno.paternostro@gmail.com"
        )

        for _item in data:
            name = _item.get("name").title()
            if (
                 name not in self.list_of_exercises
            ):  # check if exercise is repeated
               
                muscle_group = [
                    _get_or_create_obj(MuscleGroup, name=m)
                    for m in _item.get("muscle_group").split(",")
                ]

                level = _get_or_create_obj(Level, name=_item.get("level"))
                    
                exercise = Exercise.objects.get_or_create(
                    name=name,
                    description=_item.get("description"),
                    type=_get_choice_id(ExerciseTypeChoices.choices, _item.get("tipo")),
                    status=_get_choice_id(StatusChoices.choices, _item.get("status")),
                    creator=creator,
                    level=level,
                    video_link=_item.get("video_link"),
                    image="http://demo.com",
                )

                _process_list(
                    muscle_group, exercise.muscle_group
                )  # process muscle_group

                self.list_of_exercises.append(name)
                exercise.save()

