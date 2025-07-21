from ...models.appion import ApDDFrameTrajectoryData
from rest_framework import serializers

class ApDDFrameTrajectoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApDDFrameTrajectoryData
        fields = [field.name for field in ApDDFrameTrajectoryData._meta.get_fields() if not field.auto_created]