import json
import requests

from core.util import Util
from routines.models import *
from django.core.management.base import BaseCommand, CommandError


def _get_or_create_obj(klass, name, **kwargs):
    if not name:
        return None
    if len(klass.objects.filter(name=name)) == 0:
        kwargs["name"] = name
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(name=name).first()


"""def _get_tags(tags=None):
    if not tags or not isinstance(tags, list) or len(tags) == 0:
        return []
    return [_get_or_create_obj(Tag, _t) for _t in tags]"""


def _process_list(array_list, obj):
    [obj.add(_t) for _t in array_list]


def _get_data_from_gsheet():
    util = Util(google_file="1ieyGQDwG4ZDXN23ilJcdTUtdyBLM8ludxkpvLdKq34M")
    return util.get_data_from_sheet(sheet="Ejercicios")


class Command(BaseCommand):
    help = "Imports the routines from a dataset"

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

        contact_type = _get_or_create_obj(ContactType, name="phone")
        customer_type = _get_or_create_obj(CustomerType, name="trainer")
        status_type_exercise = _get_or_create_obj(StatusType, name="exercise")
        status_type_customer = _get_or_create_obj(StatusType, name="customer")
        status = _get_or_create_obj(
            Status, name="ready", status_type=status_type_customer
        )

        creator = _get_or_create_obj(
            Customer,
            name="Juan",
            surname="Paternostro",
            email="juan_pater@gmail.com",
            phone="112121111",
            contact_type=contact_type,
            status=status,
            customer_type=customer_type,
        )

        for _item in data:
            if (
                _item.get("name") not in self.list_of_exercises
            ):  # check if exercise is repeated
                training_method = _get_or_create_obj(
                    TrainingMethod, name=_item.get("training")
                )
                training = _get_or_create_obj(
                    Training,
                    name=_item.get("training"),
                    training_method=training_method,
                    description=_item.get("description"),
                )
                tipo = _get_or_create_obj(
                    ExerciseType,
                    name=_item.get("tipo"),
                    creator=creator,
                    training=training,
                )
                level = _get_or_create_obj(Level, name=_item.get("level"))
                status = _get_or_create_obj(
                    Status, name=_item.get("status"), status_type=status_type_exercise
                )

                muscle_group = _get_or_create_obj(
                    MuscleGroup, name=_item.get("muscle_group")
                )

                exercise = Exercise.objects.create(
                    name=_item.get("name"),
                    description=_item.get("descripcion"),
                    type=tipo,
                    status=status,
                    creator=creator,
                    level=level,
                    muscle_group=muscle_group,
                    video_link="",
                    image="http://demo.com",
                )

                _process_list(
                    _get_tags(_item.get("tags")), exercise.tags
                )  # process tags

                self.list_of_exercises.append(_item.get("name"))
                exercise.save()
