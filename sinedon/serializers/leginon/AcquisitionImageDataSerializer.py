from ...models.leginon import AcquisitionImageData
from rest_framework import serializers

class AcquisitionImageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcquisitionImageData
        fields = [field.name for field in AcquisitionImageData._meta.get_fields() if not field.auto_created]