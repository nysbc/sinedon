from ...models.appion import ScriptHostName
from rest_framework import serializers

class ScriptHostNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptHostName
        fields = [field.name for field in ScriptHostName._meta.get_fields() if not field.auto_created]