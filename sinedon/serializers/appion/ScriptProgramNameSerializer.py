from ...models.appion import ScriptProgramName
from rest_framework import serializers

class ScriptProgramNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptProgramName
        fields = [field.name for field in ScriptProgramName._meta.get_fields() if not field.auto_created]