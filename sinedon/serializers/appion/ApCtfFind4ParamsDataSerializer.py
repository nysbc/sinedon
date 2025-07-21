from ...models.appion import ApCtfFind4ParamsData
from rest_framework import serializers

class ApCtfFind4ParamsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApCtfFind4ParamsData
        fields = [field.name for field in ApCtfFind4ParamsData._meta.get_fields() if not field.auto_created]