from ...models.leginon import PresetData
from rest_framework import serializers
#from rest_framework.validators import UniqueTogetherValidator

class PresetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresetData
        fields = [field.name for field in PresetData._meta.get_fields() 
                  if not field.auto_created and field.get_internal_type() != "AutoField"]
        # Ideally we would use django-rest-framework's built-in validators, but for 
        # some reason the UniqueTogetherValidator sometimes returns True
        # even if there is an already existing record with the same values.
        # This appears to only occur if some of the fields are set to NULL (represented as NoneTypes) in the Python data structure.
        # Because of this issue, we're going to use our own logic to enforce uniqueness in the get/set methods for now.
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=PresetData.objects.all(),
        #         fields=[field.name for field in PresetData._meta.get_fields() 
        #           if not field.auto_created and field.get_internal_type() != "AutoField"
        #           and field.name != "def_timestamp"]
        #     )