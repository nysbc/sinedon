from ...models.leginon import NormImageData
from rest_framework import serializers

class NormImageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormImageData
        fields = [field.name for field in NormImageData._meta.get_fields() if not field.auto_created]