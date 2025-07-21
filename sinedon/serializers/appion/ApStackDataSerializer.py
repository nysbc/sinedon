from ...models.appion import ApStackData
from rest_framework import serializers

class ApStackDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApStackData
        fields = [field.name for field in ApStackData._meta.get_fields() if not field.auto_created]