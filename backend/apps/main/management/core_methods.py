from apps.main.util import Util


from googletrans import Translator, constants

from ..constants import LanguagesChoices

def _get_choice_id(choice, searching_value):
    return [c[0] for c in choice if c[1].lower() == searching_value.lower()][0]

def _get_or_create_obj_by_id(klass, id, **kwargs):
    if not id:
        return None
    if len(klass.objects.filter(id=id)) == 0:
        kwargs["id"] = id
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(id=id).first()


def _get_or_create_obj(klass, name, **kwargs):
    if not name:
        return None
    if len(klass.objects.filter(name=name)) == 0:
        kwargs["name"] = name
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(name=name).first()


def _get_or_create_customer(klass, customer, **kwargs):
    if not customer:
        return None
    if len(klass.objects.filter(customer=customer)) == 0:
        kwargs["customer"] = customer
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(customer=customer).first()


def _get_or_create_user(klass, email, **kwargs):
    if not email:
        return None
    if len(klass.objects.filter(email=email)) == 0:
        kwargs["email"] = email
        obj = klass.objects.create(**kwargs)
        return obj
    return klass.objects.filter(email=email).first()


"""def _get_tags(tags=None):
    if not tags or not isinstance(tags, list) or len(tags) == 0:
        return []
    return [_get_or_create_obj(Tag, _t) for _t in tags]"""


def _process_list(array_list, obj):
    [obj.add(_t) for _t in array_list]


def _get_data_from_gsheet(file_id, sheet):
    util = Util(google_file=file_id)
    return util.get_data_from_sheet(sheet=sheet)
