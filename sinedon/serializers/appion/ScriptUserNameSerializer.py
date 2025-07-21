from ...models.appion import ScriptUserName
from rest_framework import serializers

class ScriptUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptUserName
        fields = [field.name for field in ScriptUserName._meta.get_fields() if not field.auto_created]