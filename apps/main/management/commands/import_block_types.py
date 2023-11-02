from ...constants import LanguagesChoices
from apps.main.util import Util
from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _process_list,
)

from googletrans import Translator, constants

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
    return util.get_data_from_sheet(sheet="block_type")


class Command(BaseCommand):
    help = "Imports the customers from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet()
        translator = Translator()
        for _item in data:
            
            block_type = _get_or_create_obj(
                BlockType,
                name=_item.get("name"),
                image=_item.get("image")
            )
            
            block_type.save()
            for l in LanguagesChoices.choices:
                lang = l[0]
                value_to_translate = _item.get("name")
                traslation = translator.translate(value_to_translate, dest=lang)
                block_type_lang = BlockTypeLang.objects.create(
                    lang = _get_or_create_obj(Language, name=l[1].lower()),
                    translation = traslation.text.lower(),
                    block_type = _get_or_create_obj(BlockType, name=value_to_translate)
                )
                block_type_lang.save()