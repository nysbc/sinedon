from .private import _getModel, _getSerializer
from django.db.models import F

def get(model_name : str, data : dict = {}):
    model=_getModel(model_name)
    if not model:
        raise RuntimeError("No model exists with name %s." % model_name)
    serializer=_getSerializer(model_name)
    if not serializer:
        raise RuntimeError("No serializer exists for model named %s." % model_name)
    try:
        record=model.objects.get(**data)
    except model.MultipleObjectsReturned:
        record=model.objects.filter(**data).order_by(F("def_timestamp").desc())[0]
    except model.DoesNotExist:
        return {}
    ser=serializer(record)
    return ser.data
