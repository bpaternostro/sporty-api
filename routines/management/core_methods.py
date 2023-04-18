from core.util import Util


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


"""def _get_tags(tags=None):
    if not tags or not isinstance(tags, list) or len(tags) == 0:
        return []
    return [_get_or_create_obj(Tag, _t) for _t in tags]"""


def _process_list(array_list, obj):
    [obj.add(_t) for _t in array_list]


def _get_data_from_gsheet(file_id, sheet):
    util = Util(google_file=file_id)
    return util.get_data_from_sheet(sheet=sheet)
