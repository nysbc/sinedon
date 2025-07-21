from ...models.leginon import ObjIceThicknessData
from rest_framework import serializers

class ObjIceThicknessDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjIceThicknessData
        fields = [field.name for field in ObjIceThicknessData._meta.get_fields() if not field.auto_created]