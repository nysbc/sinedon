from ...models.appion import ApAssessmentData
from rest_framework import serializers

class ApAssessmentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApAssessmentData
        fields = [field.name for field in ApAssessmentData._meta.get_fields() if not field.auto_created]