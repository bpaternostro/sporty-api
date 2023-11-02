from apps.main.util import Util
from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
)

def _get_or_create_obj(klass, name, **kwargs):
    if not name:
        return None
    if len(klass.objects.filter(name=name)) == 0:
        kwargs["name"] = name
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(name=name).first()


def _get_data_from_gsheet():
    util = Util(google_file="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM")
    return util.get_data_from_sheet(sheet="lang")


class Command(BaseCommand):
    help = "Imports the customers from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet()
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

        for _item in data:
            status = _get_or_create_obj(
                LanguageStatus, name=_item.get("status")
            )
            
            lang = _get_or_create_obj(
                Language,
                name=_item.get("name"),
                code=_item.get("code"),
                status=status,
                encoding=_item.get("encoding"),
            )
            
            lang.save()
