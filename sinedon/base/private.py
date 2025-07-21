import sinedon.serializers.appion as appion_serializers
import sinedon.serializers.leginon as leginon_serializers
import sinedon.models.appion as appion_models
import sinedon.models.leginon as leginon_models

def _getSerializer(model_name: str):
    serializer_name="%sSerializer" % model_name
    serializer=None
    for serializers in [appion_serializers, leginon_serializers]:
        try:
            serializer=getattr(serializers, serializer_name)
        except AttributeError:
            continue
    return serializer

def _getModel(model_name: str):
    model=None
    for models in [appion_models, leginon_models]:
        try:
            model=getattr(models, model_name)
        except AttributeError:
            continue
    return model
