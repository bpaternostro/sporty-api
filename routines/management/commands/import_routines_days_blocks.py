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

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1ieyGQDwG4ZDXN23ilJcdTUtdyBLM8ludxkpvLdKq34M",
            sheet="RoutinesDaysBlocks",
        )
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

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
