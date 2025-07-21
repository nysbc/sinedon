from ...models.appion import ApCtfData
from rest_framework import serializers

class ApCtfDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApCtfData
        fields = [field.name for field in ApCtfData._meta.get_fields() if not field.auto_created]