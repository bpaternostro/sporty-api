
from apps.routines.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_or_create_obj, _process_list

from ...constants import LanguagesChoices
from googletrans import Translator, constants

class Command(BaseCommand):
    help = "Imports the muscle groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_muscle_group = (
            []
        )  # creates an auxiliar list to check if muscle_group is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM",
            sheet="muscle_group",
        )

        translator = Translator()

        for _item in data:
            if (
                _item.get("name") not in self.list_of_muscle_group
            ):  # check if muscle_group is repeated
                muscle_group_type = _get_or_create_obj(
                    MuscleGroupType, name=_item.get("type"), image=""
                )

                muscle_group = MuscleGroup.objects.create(
                    name=_item.get("name"),
                    muscle_group_type=muscle_group_type,
                    image=_item.get("image"),
                )

                self.list_of_muscle_group.append(_item.get("name"))

                muscle_group = muscle_group.save()

                for l in LanguagesChoices.choices:
                    lang = l[0]
                    value_to_translate = _item.get("name")
                    traslation = translator.translate(value_to_translate, dest=lang)
                    muscle_group_lang = MuscleGroupLang.objects.create(
                        lang = _get_or_create_obj(Language, name=l[1].lower()),
                        translation = traslation.text.lower(),
                        muscle_group = _get_or_create_obj(MuscleGroup, name=value_to_translate)
                    )
                    muscle_group_lang.save()