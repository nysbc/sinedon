from ...models.leginon import CorrectorPlanData
from rest_framework import serializers

class CorrectorPlanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectorPlanData
        fields = [field.name for field in CorrectorPlanData._meta.get_fields() if not field.auto_created]