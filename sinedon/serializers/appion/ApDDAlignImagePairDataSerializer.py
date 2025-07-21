from ...models.appion import ApDDAlignImagePairData
from rest_framework import serializers

class ApDDAlignImagePairDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApDDAlignImagePairData
        fields = [field.name for field in ApDDAlignImagePairData._meta.get_fields() if not field.auto_created]