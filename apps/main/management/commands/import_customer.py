from apps.main.util import Util
from apps.routines.models import *
from apps.customers.models import *
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
    return util.get_data_from_sheet(sheet="customers")


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
        data = _get_data_from_gsheet()
        # if res.status_code != 200:
        #    raise CommandError("Cannot retrieve dataset, please try later!")

        for _item in data:
            contact_type = _get_or_create_obj(ContactType, name=_item.get("contact_type"))
            customer_type = _get_or_create_obj(CustomerType, name=_item.get("customer_type"))
            level = _get_or_create_obj(Level, name=_item.get("level"))
            status = _get_or_create_obj(
                CustomerStatus, name=_item.get("status")
            )
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
            customer = _get_or_create_obj(
                Customer,
                name=_item.get("name"),
                surname=_item.get("surname"),
                username=_item.get("username"),
                email=_item.get("email"),
                phone=_item.get("phone"),
                level=level,
                contact_type=contact_type,
                status=status,
                customer_type=customer_type,
                lang=_get_or_create_obj(Language, name=_item.get("lang"))
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
