import json
import requests

from apps.main.util import Util
from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import _get_data_from_gsheet, _get_or_create_obj

from ...constants import LanguagesChoices, CODE_LANGS
from googletrans import Translator, constants

class Command(BaseCommand):
    help = "Imports the muscle groups from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
       
        def set_customer_status_lang(lang, value_to_translate, traslation): 
            obj_lang = CustomerStatusLang.objects.create(
                        lang = _get_or_create_obj(Language, name=lang),
                        translation = traslation.text.lower(),
                        customer_status = _get_or_create_obj(CustomerStatus, name=value_to_translate))
            obj_lang.save()
        
        def set_block_status_lang(lang, value_to_translate, traslation): 
            obj_lang = BlockStatusLang.objects.create(
                        lang = _get_or_create_obj(Language, name=lang),
                        translation = traslation.text.lower(),
                        block_status = _get_or_create_obj(BlockStatus, name=value_to_translate))
            obj_lang.save()
        
        def set_exercise_status_lang(lang, value_to_translate, traslation): 
            obj_lang = ExerciseStatusLang.objects.create(
                        lang = _get_or_create_obj(Language, name=lang),
                        translation = traslation.text.lower(),
                        exercise_status = _get_or_create_obj(ExerciseStatus, name=value_to_translate))
            obj_lang.save()
        
        def set_routine_status_lang(lang, value_to_translate, traslation): 
            obj_lang = RoutineStatusLang.objects.create(
                        lang = _get_or_create_obj(Language, name=lang),
                        translation = traslation.text.lower(),
                        routine_status = _get_or_create_obj(RoutineStatus, name=value_to_translate))
            obj_lang.save()

        def set_routine_customer_status_lang(lang, value_to_translate, traslation): 
            obj_lang = RoutineCustomerStatusLang.objects.create(
                        lang = _get_or_create_obj(Language, name=lang),
                        translation = traslation.text.lower(),
                        routine_customer_status = _get_or_create_obj(RoutineCustomerStatus, name=value_to_translate))
            obj_lang.save()

        def get_status(stat):
            return _get_data_from_gsheet(
                file_id="1IRu0coOANYi5Qn_zAxg8JfcevNG8_gJl__oseM2GRtM",
                sheet=stat,
            )
        
        translator = Translator()
        status_tables={
            (CustomerStatus, set_customer_status_lang) :"customer_status",
            (BlockStatus, set_block_status_lang):"customer_status",
            (ExerciseStatus, set_exercise_status_lang):"exercise_status",
            (RoutineStatus, set_routine_status_lang):"routine_status",
            (RoutineCustomerStatus, set_routine_customer_status_lang):"customer_routine_status",
        }
        
        for k,v in status_tables.items():
            for _item in get_status(v):
                status = k[0].objects.create(
                    name=_item.get("name"),
                    description=_item.get("description")
                )
                status.save()
                for l in LanguagesChoices.choices:
                    lang = l[0]
                    value_to_translate = _item.get("name")
                    traslation = translator.translate(value_to_translate, dest=lang)
                    k[1](CODE_LANGS.get(lang), value_to_translate, traslation)
                    
