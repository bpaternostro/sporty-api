from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
    _get_or_create_obj_by_id,
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
            file_id="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM",
            sheet="blocks_exercises",
        )
        
        translator = Translator()

        status = _get_or_create_obj(BlockStatus, name="ready")
        for _item in data:
            creator = _get_or_create_obj_by_id(Customer, id=_item.get("creator"))
            type = _get_or_create_obj(BlockType, name=_item.get("type"))
            block = _get_or_create_obj(
                Block, name=_item.get("block"), status=status, creator=creator, type=type
            )
            
            block_exercise_detail = BlockExerciseDetail.objects.create(
                block = block,
                exercise=_get_or_create_obj(Exercise, name=_item.get("exercise")),
                serie=_item.get("serie"),
                reps=_item.get("reps"),
                weight=_item.get("weight"),
                pause=_item.get("pause"),
                observation=_item.get("observation"),
            )
            
            block_exercise_detail.save()
            
            for l in LanguagesChoices.choices:
                lang = l[0]
                value_to_translate = _item.get("block")
                traslation = translator.translate(value_to_translate, dest=lang)
                block_lang = BlockLang.objects.create(
                    lang = _get_or_create_obj(Language, name=l[1].lower()),
                    translation = traslation.text.lower(),
                    block = _get_or_create_obj(Block, name=value_to_translate)
                )
                block_lang.save()

                # TODO poner bien los inlines de languages