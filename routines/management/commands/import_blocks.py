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
    help = "Imports blocks from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_blocks = (
            []
        )  # creates an auxiliar list to check if list_of_blocks is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1ieyGQDwG4ZDXN23ilJcdTUtdyBLM8ludxkpvLdKq34M",
            sheet="blocks_exercises",
        )
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

        status_type_block = _get_or_create_obj(StatusType, name="block")
        status = _get_or_create_obj(Status, name="ready", status_type=status_type_block)
        for _item in data:
            creator = _get_or_create_obj_by_id(Customer, id=_item.get("creator"))
            block = _get_or_create_obj(
                Block, name=_item.get("block"), status=status, creator=creator
            )

            blockExercise = BlockExercise.objects.create(
                block=block,
                exercise=_get_or_create_obj(Exercise, name=_item.get("exercise")),
                serie=_item.get("serie"),
                reps=_item.get("reps"),
                weight=_item.get("weight"),
                pause=_item.get("pause"),
                observation=_item.get("observation"),
            )

            blockExercise.save()
