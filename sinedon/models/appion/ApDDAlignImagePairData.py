# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
from ..leginon import AcquisitionImageData
from .ApDDStackRunData import ApDDStackRunData

class ApDDAlignImagePairData(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    ref_acquisitionimagedata_source = models.IntegerField(
        db_column="REF|AcquisitionImageData|source",
        blank=True,
        null=True,
    )
    ref_acquisitionimagedata_result = models.IntegerField(
        db_column="REF|AcquisitionImageData|result",
        blank=True,
        null=True,
    )
    ref_apddstackrundata_ddstackrun = models.IntegerField(
        db_column="REF|ApDDStackRunData|ddstackrun",
        blank=True,
        null=True,
    )
    class Meta:
        managed = False
        verbose_name = "ApDDAlignImagePairData"
        verbose_name_plural = "ApDDAlignImagePairData"
        db_table = "ApDDAlignImagePairData"