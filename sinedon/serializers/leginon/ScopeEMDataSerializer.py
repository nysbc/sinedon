from ...models.leginon import ScopeEMData
from rest_framework import serializers

class ScopeEMDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScopeEMData
        fields = [field.name for field in ScopeEMData._meta.get_fields() if not field.auto_created]