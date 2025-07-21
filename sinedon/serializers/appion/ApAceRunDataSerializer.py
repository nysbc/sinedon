from ...models.appion import ApAceRunData
from rest_framework import serializers

class ApAceRunDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApAceRunData
        fields = [field.name for field in ApAceRunData._meta.get_fields() if not field.auto_created]