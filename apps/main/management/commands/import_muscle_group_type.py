
from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_or_create_obj, _process_list

from ...constants import LanguagesChoices
from googletrans import Translator, constants

class Command(BaseCommand):
    help = "Imports muscle_group_type from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM",
            sheet="muscle_group_type",
        )

        translator = Translator()

        for _item in data:

            muscle_group_type = MuscleGroupType.objects.create(
                name=_item.get("name"),
                image=_item.get("image"),
            )

            muscle_group_type.save()

            for l in LanguagesChoices.choices:
                lang = l[0]
                value_to_translate = _item.get("name")
                traslation = translator.translate(value_to_translate, dest=lang)
                muscle_group_type_lang = MuscleGroupTypeLang.objects.create(
                    lang = _get_or_create_obj(Language, name=l[1].lower()),
                    translation = traslation.text.lower(),
                    muscle_group_type = _get_or_create_obj(MuscleGroupType, name=value_to_translate)
                )
                muscle_group_type_lang.save()