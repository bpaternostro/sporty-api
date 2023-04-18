import json
import requests

from core.util import Util
from routines.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
    _get_or_create_obj_by_id,
)


class Command(BaseCommand):
    help = "Imports the routines groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.routines = (
            []
        )  # creates an auxiliar list to check if muscle_group is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1ieyGQDwG4ZDXN23ilJcdTUtdyBLM8ludxkpvLdKq34M",
            sheet="Routines",
        )
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

        for _item in data:
            if (
                _item.get("name") not in self.routines
            ):  # check if muscle_group is repeated
                routine_type = _get_or_create_obj(
                    RoutineType, name=_item.get("routine_type")
                )

                level = _get_or_create_obj(Level, name=_item.get("level"))

                creator = _get_or_create_obj_by_id(Customer, id=_item.get("creator"))

                system = _get_or_create_obj(System, name=_item.get("system"))

                cadence = _get_or_create_obj(Cadence, name=_item.get("cadence"))

                restrictions = [
                    _get_or_create_obj(Restriction, name=m)
                    for m in _item.get("restrictions").split(",")
                ]

                goals = [
                    _get_or_create_obj(Goal, name=m)
                    for m in _item.get("goals").split(",")
                ]

                routine = Routine.objects.create(
                    name=_item.get("name"),
                    description=_item.get("description"),
                    routine_type=routine_type,
                    level=level,
                    creator=creator,
                    system=system,
                    cadence=cadence,
                    warm_up=_item.get("warm_up"),
                    cardio=_item.get("cardio"),
                    duration=_item.get("duration"),
                    pre_exhaustion=_item.get("pre_exhaustion"),
                    activation=_item.get("activation"),
                    rest_between_exercises=_item.get("rest_between_exercises"),
                )

                _process_list(
                    restrictions, routine.restrictions
                )  # process restrictions

                _process_list(goals, routine.goals)  # process goals

                self.routines.append(_item.get("name"))
                routine.save()
