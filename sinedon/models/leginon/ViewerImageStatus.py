# SPDX-License-Identifier: Apache-2.0
# Copyright 2023-2025 New York Structural Biology Center

from django.db import models
from .AcquisitionImageData import AcquisitionImageData
from .SessionData import SessionData

class ViewerImageStatus(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    status = models.TextField(blank=True, null=True)
    ref_acquisitionimagedata_image = models.ForeignKey(
        AcquisitionImageData,
        db_column="REF|AcquisitionImageData|image",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    ref_sessiondata_session = models.ForeignKey(
        SessionData,
        db_column="REF|SessionData|session",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        managed = False
        db_table = "ViewerImageStatus"
        verbose_name_plural = "ViewerImageStatus"
        verbose_name = "ViewerImageStatus"
