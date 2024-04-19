import os

from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from apps.authentication.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
    _get_or_create_user,
    _get_choice_id
)

from ...constants import LanguagesChoices
from googletrans import Translator, constants

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
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="blocks_exercises",
        )
        for _item in data:
            creator = _get_or_create_user(CustomUser, email="bruno.paternostro@gmail.com")
            block = _get_or_create_obj(
                Block, name=_item.get("block"), creator=creator, type=_get_choice_id(BlockTypeChoices.choices, _item.get("type"))
            )
            
            block_exercise_detail = BlockExerciseDetail.objects.create(
                block = block,
                exercise=_get_or_create_obj(Exercise, name=_item.get("exercise").title()),
                serie=_item.get("serie"),
                reps=_item.get("reps"),
                weight=_item.get("weight"),
                time=_item.get("time"),
                pause=_item.get("pause"),
                observation=_item.get("observation"),
            )
            
            block_exercise_detail.save()