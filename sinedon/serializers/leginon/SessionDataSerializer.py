from ...models.leginon import SessionData
from rest_framework import serializers

class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionData
        fields = [field.name for field in SessionData._meta.get_fields() if not field.auto_created]