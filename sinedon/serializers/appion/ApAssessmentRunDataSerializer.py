from ...models.appion import ApAssessmentRunData
from rest_framework import serializers

class ApAssessmentRunDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApAssessmentRunData
        fields = [field.name for field in ApAssessmentRunData._meta.get_fields() if not field.auto_created]