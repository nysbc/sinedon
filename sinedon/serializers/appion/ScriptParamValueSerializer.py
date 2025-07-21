from ...models.appion import ScriptParamValue
from rest_framework import serializers

class ScriptParamValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptParamValue
        fields = [field.name for field in ScriptParamValue._meta.get_fields() if not field.auto_created]