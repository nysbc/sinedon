from ...models.leginon import InstrumentData
from rest_framework import serializers

class InstrumentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstrumentData
        fields = [field.name for field in InstrumentData._meta.get_fields() if not field.auto_created]