from ...models.appion import poster
from rest_framework import serializers

class posterSerializer(serializers.ModelSerializer):
    class Meta:
        model = poster
        fields = [field.name for field in poster._meta.get_fields() if not field.auto_created]