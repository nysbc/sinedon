from ...models.leginon import ViewerImageStatus
from rest_framework import serializers

class ViewerImageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewerImageStatus
        fields = [field.name for field in ViewerImageStatus._meta.get_fields() if not field.auto_created]