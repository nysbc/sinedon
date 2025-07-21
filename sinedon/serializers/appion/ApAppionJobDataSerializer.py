from ...models.appion import ApAppionJobData
from rest_framework import serializers

class ApAppionJobDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApAppionJobData
        fields = [field.name for field in ApAppionJobData._meta.get_fields() if not field.auto_created]