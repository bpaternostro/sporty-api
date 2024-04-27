import os

from apps.main.util import Util
from apps.routines.models import *
from apps.main.models import *
from apps.customers.models import Customer
from apps.authentication.models import CustomUser

from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
    _get_or_create_user,
    _get_choice_id
)


class Command(BaseCommand):
    help = "Imports the routines groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.routines = (
            []
        )  # creates an auxiliar list to check if muscle_group is repeated

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="routines",
        )

        for _item in data:
            if (
                _item.get("name") not in self.routines
            ):  # check if muscle_group is repeated
                
                routine_type = _get_choice_id(RoutineTypeChoices.choices, _item.get("routine_type"))

                status = _get_choice_id(StatusChoices.choices, _item.get("status"))

                creator = _get_or_create_user(CustomUser, email="bruno.paternostro@gmail.com")
                
                system = _get_choice_id(SystemChoices.choices, _item.get("system"))

                cadence = _get_choice_id(CadenceChoices.choices, _item.get("cadence"))

                training_method = _get_choice_id(TrainingMethodChoices.choices, _item.get("training_method"))

                restrictions = [
                    _get_or_create_obj(Restriction, name=m)
                    for m in _item.get("restrictions").split(",")
                ]

                routine = _get_or_create_obj(Routine,
                    name=_item.get("name"),
                    description=_item.get("description"),
                    routine_type=routine_type,
                    status=status,
                    creator=creator,
                    system=system,
                    cadence=cadence,
                    cardio=_item.get("cardio"),
                    duration=_item.get("duration"),
                    pre_exhaustion=_get_choice_id(YesNoChoices.choices, _item.get("pre_exhaustion")),
                    activation=_get_choice_id(YesNoChoices.choices, _item.get("activation")),
                    rest_between_exercises=_item.get("rest_between_exercises"),
                    training_method=training_method,
                )

                _process_list(
                    restrictions, routine.restrictions
                )  # process restrictions


                self.routines.append(_item.get("name"))
                routine.save()
