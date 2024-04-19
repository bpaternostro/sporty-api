import os

from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet

class Command(BaseCommand):
    help = "Imports levels from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="levels",
        )

        for _item in data:

            level = Level.objects.create(
                name=_item.get("name"),
                image=_item.get("image"),
            )

            level.save()
