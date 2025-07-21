from ...models.leginon import PixelSizeCalibrationData
from rest_framework import serializers

class PixelSizeCalibrationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PixelSizeCalibrationData
        fields = [field.name for field in PixelSizeCalibrationData._meta.get_fields() if not field.auto_created]