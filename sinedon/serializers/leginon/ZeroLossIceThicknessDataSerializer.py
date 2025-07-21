from ...models.leginon import ZeroLossIceThicknessData
from rest_framework import serializers

class ZeroLossIceThicknessDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeroLossIceThicknessData
        fields = [field.name for field in ZeroLossIceThicknessData._meta.get_fields() if not field.auto_created]