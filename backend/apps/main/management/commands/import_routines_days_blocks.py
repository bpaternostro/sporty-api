import os

from apps.main.util import Util
from apps.routines.models import *
from apps.main.models import *
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

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="routines_days_blocks",
        )

        for _item in data:
            blocks = [
                _get_or_create_obj_by_id(Block, id=int(m))
                for m in _item.get("blocks").split("-")
            ]
            day = _get_or_create_obj(Day, name=_item.get("day"))
            
            routineDaysBlocks = RoutineDaysBlocks.objects.create(
                routine=_get_or_create_obj_by_id(Routine, id=_item.get("routine")),
                day = day
            )

            _process_list(blocks, routineDaysBlocks.blocks)  # process blocks

            routineDaysBlocks.save()
