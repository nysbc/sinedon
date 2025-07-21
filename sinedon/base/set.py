from .private import _getSerializer, _getModel

def set(model_name : str, data : dict) -> bool:
    model=_getModel(model_name)
    if not model:
        raise RuntimeError("No model exists with name %s." % model_name)
    serializer=_getSerializer(model_name)
    if not serializer:
        raise RuntimeError("No serializer exists for model named %s." % model_name)
    deser=serializer(data=data)
    # We perform our own validation logic here because UniqueTogetherValidator doesn't 
    # seem to work reliably for our purposes (see note in PresetDataSerializer).
    valid_fields=[field.name for field in model._meta.get_fields() 
                  if not field.auto_created and field.get_internal_type() != "AutoField"
                  and field.name != "def_timestamp"]
    filtered_data={k : v for k,v in data.items() if k in valid_fields}
    queryset=model.objects.filter(**filtered_data)
    if not queryset:
        deser.is_valid()
        deser.save()
        return True
    return False