import os

from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_choice_id, _get_or_create_obj

class Command(BaseCommand):
    help = "Imports the muscle groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_muscle_group = (
            []
        )  # creates an auxiliar list to check if muscle_group is repeated


    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="muscle_group",
        )

        for _item in data:
            if (
                _item.get("name") not in self.list_of_muscle_group
            ):  # check if muscle_group is repeated

                muscle_group = _get_or_create_obj(MuscleGroup,
                    name=_item.get("name"),
                    muscle_group_type=_get_choice_id(MuscleGroupTypeChoices.choices, _item.get("type")),
                    image=_item.get("image"),
                )

                self.list_of_muscle_group.append(_item.get("name"))

                muscle_group = muscle_group.save()
