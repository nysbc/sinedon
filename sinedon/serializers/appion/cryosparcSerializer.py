from ...models.appion import cryosparc
from rest_framework import serializers

class cryosparcSerializer(serializers.ModelSerializer):
    class Meta:
        model = cryosparc
        fields = [field.name for field in cryosparc._meta.get_fields() if not field.auto_created]