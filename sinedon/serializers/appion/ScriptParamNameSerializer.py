from ...models.appion import ScriptParamName
from rest_framework import serializers

class ScriptParamNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptParamName
        fields = [field.name for field in ScriptParamName._meta.get_fields() if not field.auto_created]