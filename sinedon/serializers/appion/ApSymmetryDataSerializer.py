from ...models.appion import ApSymmetryData
from rest_framework import serializers

class ApSymmetryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApSymmetryData
        fields = [field.name for field in ApSymmetryData._meta.get_fields() if not field.auto_created]