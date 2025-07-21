from ...models.appion import ApPathData
from rest_framework import serializers

class ApPathDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApPathData
        fields = [field.name for field in ApPathData._meta.get_fields() if not field.auto_created]