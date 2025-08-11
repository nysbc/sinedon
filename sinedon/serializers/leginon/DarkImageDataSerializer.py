from ...models.leginon import DarkImageData
from rest_framework import serializers

class DarkImageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarkImageData
        fields = [field.name for field in DarkImageData._meta.get_fields() if not field.auto_created]