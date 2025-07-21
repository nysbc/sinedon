from ...models.appion import ScriptProgramRun
from rest_framework import serializers

class ScriptProgramRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptProgramRun
        fields = [field.name for field in ScriptProgramRun._meta.get_fields() if not field.auto_created]