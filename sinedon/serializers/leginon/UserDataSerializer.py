from ...models.leginon import UserData
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [field.name for field in UserData._meta.get_fields() if not field.auto_created]