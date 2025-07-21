from .private import _getModel, _getSerializer

def get(model_name : str, data : dict = {}):
    model=_getModel(model_name)
    if not model:
        raise RuntimeError("No model exists with name %s." % model_name)
    serializer=_getSerializer(model_name)
    if not serializer:
        raise RuntimeError("No serializer exists for model named %s." % model_name)
    try:
        record=model.object.get(**data)
    except Exception:
        return {}
    ser=serializer(record)
    return ser.data