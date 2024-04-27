import os

from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_or_create_obj, _process_list


class Command(BaseCommand):
    help = "Imports days from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="days",
        )

        for _item in data:
            _get_or_create_obj(Day,name=_item.get("name"))