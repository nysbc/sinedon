from ...models.appion import ApCtfTiltParamsData
from rest_framework import serializers

class ApCtfTiltParamsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApCtfTiltParamsData
        fields = [field.name for field in ApCtfTiltParamsData._meta.get_fields() if not field.auto_created]