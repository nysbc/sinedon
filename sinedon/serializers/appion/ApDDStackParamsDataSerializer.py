from ...models.appion import ApDDStackParamsData
from rest_framework import serializers

class ApDDStackParamsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApDDStackParamsData
        fields = [field.name for field in ApDDStackParamsData._meta.get_fields() if not field.auto_created]