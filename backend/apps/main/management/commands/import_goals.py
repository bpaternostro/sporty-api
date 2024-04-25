import os

from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet

class Command(BaseCommand):
    help = "Imports goals from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="goals",
        )

        for _item in data:

            goal = Goal.objects.get_or_create(
                name=_item.get("name"),
                image=_item.get("image"),
            )

            goal.save()
