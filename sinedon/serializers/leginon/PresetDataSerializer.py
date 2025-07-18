from ...models.leginon import PresetData
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class PresetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresetData
        fields = [field.name for field in PresetData._meta.get_fields() 
                  if not field.auto_created and field.get_internal_type() != "AutoField"]
        validators = [
            UniqueTogetherValidator(
                queryset=PresetData.objects.all(),
                fields=[field.name for field in PresetData._meta.get_fields() 
                  if not field.auto_created and field.get_internal_type() != "AutoField"
                  and field.name != "def_timestamp"]
                #fields=["name","ref_instrumentdata_tem"]
                #fields=['ref_sessiondata_session', 'number', 'name', 'skip', 'removed', 
                #        'hasref', 'ref_instrumentdata_tem', 'projection_mode', 'magnification', 
                #        'spot_size', 'intensity', 'image_shift_x', 'image_shift_y', 'beam_shift_x', 
                #        'beam_shift_y', 'diffraction_shift_x', 
                #        'diffraction_shift_y', 
                #        'defocus']#, 
                        #'defocus_range_min'] 
                        #'defocus_range_max', 'dose', 'tem_energy_filter', 'tem_energy_filter_width', 'probe_mode']#, 
                        #'ref_instrumentdata_ccdcamera', 'exposure_time', 'dimension_x', 'dimension_y']#, 
                        #'binning_x', 'binning_y', 'offset_x', 'offset_y', 'energy_filter', 'energy_filter_width']#, 
                        #'energy_filter_offset', 'pre_exposure', 'alt_channel', 'save_frames', 'frame_time']#, 
                        #'request_nframes', 'align_frames', 'align_filter', 'use_frames', 'readout_delay', 'fast_save']#, 
                        #'use_cds']
            )
        ]