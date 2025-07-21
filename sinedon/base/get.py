from .private import _getModel, _getSerializer

def get(model_name : str, def_id : int):
    model=_getModel(model_name)
    if not model:
        raise RuntimeError("No model exists with name %s." % model_name)
    serializer=_getSerializer(model_name)
    if not serializer:
        raise RuntimeError("No serializer exists for model named %s." % model_name)
    try:
        record=model.objects.get(def_id=def_id)
    except Exception as e:
        raise RuntimeError("Could not retrieve row for %d." % def_id) from e
    ser=serializer(record)
    return ser.data