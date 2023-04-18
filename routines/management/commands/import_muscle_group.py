import json
import requests

from core.util import Util
from routines.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_or_create_obj


class Command(BaseCommand):
    help = "Imports the muscle groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_muscle_group = (
            []
        )  # creates an auxiliar list to check if muscle_group is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1ieyGQDwG4ZDXN23ilJcdTUtdyBLM8ludxkpvLdKq34M",
            sheet="Grupos Musculares",
        )
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

        for _item in data:
            if (
                _item.get("name") not in self.list_of_muscle_group
            ):  # check if muscle_group is repeated
                muscle_group_type = _get_or_create_obj(
                    MuscleGroupType, name=_item.get("type"), image=""
                )

                muscle_group = MuscleGroup.objects.create(
                    name=_item.get("name"),
                    muscle_group_type=muscle_group_type,
                    image=_item.get("image"),
                )

                self.list_of_muscle_group.append(_item.get("name"))
                muscle_group.save()
