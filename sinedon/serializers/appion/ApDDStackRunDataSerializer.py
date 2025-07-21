from ...models.appion import ApDDStackRunData
from rest_framework import serializers

class ApDDStackRunDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApDDStackRunData
        fields = [field.name for field in ApDDStackRunData._meta.get_fields() if not field.auto_created]