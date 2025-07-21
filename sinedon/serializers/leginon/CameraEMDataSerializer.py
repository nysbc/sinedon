from ...models.leginon import CameraEMData
from rest_framework import serializers

class CameraEMDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraEMData
        fields = [field.name for field in CameraEMData._meta.get_fields() if not field.auto_created]