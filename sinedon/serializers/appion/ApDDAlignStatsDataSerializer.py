from ...models.appion import ApDDAlignStatsData
from rest_framework import serializers

class ApDDAlignStatsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApDDAlignStatsData
        fields = [field.name for field in ApDDAlignStatsData._meta.get_fields() if not field.auto_created]