import os

from apps.routines.models import *
from apps.customers.models import *
from apps.main.models import *
from apps.authentication.models import *
from django.core.management.base import BaseCommand, CommandError
from ..core_methods import (
    _get_data_from_gsheet,
    _get_or_create_obj,
    _get_or_create_user,
    _process_list,
    _get_choice_id,
    _get_or_create_customer
)

from ....customers.constants import *


class Command(BaseCommand):
    help = "Imports the customers from a dataset"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_of_exercises = (
            []
        )  # creates an auxiliar list to check if book is repeated

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        """ """
        data = _get_data_from_gsheet(
            file_id=os.getenv("GOOGLE_SHEET"),
            sheet="customers",
        )

        for _item in data:
            
            goals = [
                    _get_or_create_obj(Goal, name=m)
                    for m in _item.get("goals").split(",")
            ]

            restrictions = [
                    _get_or_create_obj(Restriction, name=m)
                    for m in _item.get("restrictions").split(",")
            ]
            trainings_preferences = [
                    _get_or_create_obj(Training, name=m)
                    for m in _item.get("trainings_preferences").split(",")
            ]
            
            level = _get_or_create_obj(Level, name=_item.get("level"))
            
            username = _get_or_create_user(CustomUser, email=_item.get("username"), last_name=_item.get("surname"),
                first_name= _item.get("name"),
                username=_item.get("username"),
                password="holis"
            )

            customer = _get_or_create_customer(
                Customer,
                customer=username,
                level=level,

            )
            
            _process_list(
                restrictions, customer.restrictions
            )  # process restrictions
            
            _process_list(
                    goals, customer.goals
            )  # process goals

            _process_list(
                    trainings_preferences, customer.trainings_preferences
            )  # process trainings_preferences

            customer.save()