# SPDX-License-Identifier: Apache-2.0
# Copyright 2023-2025 New York Structural Biology Center

from django.db import models
from .AcquisitionImageData import AcquisitionImageData

class ObjIceThicknessData(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    ref_acquisitionimagedata_image = models.ForeignKey(
        AcquisitionImageData,
        db_column="REF|AcquisitionImageData|image",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    vacuum_intensity = models.FloatField(db_column="vacuum intensity", blank=True, null=True)
    mfp = models.FloatField(blank=True, null=True)
    intensity = models.FloatField(blank=True, null=True)
    thickness = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        verbose_name = "ObjIceThicknessData"
        verbose_name_plural = "ObjIceThicknessData"
        db_table = "ObjIceThicknessData"