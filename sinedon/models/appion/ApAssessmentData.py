# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
from .ApAssessmentRunData import ApAssessmentRunData

class ApAssessmentData(models.Model):
	def_id = models.AutoField(db_column="DEF_id", primary_key=True)
	def_timestamp = models.DateTimeField(
		db_column="DEF_timestamp", auto_now_add=True
	)
	ref_apassessmentrundata_assessmentrun = models.ForeignKey(
        ApAssessmentRunData,
        db_column="REF|ApAssessmentRunData|assessmentrun",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
	ref_acquisitionimagedata_image = models.IntegerField(
		db_column="REF|leginondata|AcquisitionImageData|image",
		blank=True,
		null=True,
	)
	selectionkeep = models.IntegerField(blank=True, null=True)
	
	name = models.TextField(blank=True,null=True)
	class Meta:
		managed = False
		verbose_name = "ApAssessmentData"
		verbose_name_plural = "ApAssessmentData"
		db_table = "ApAssessmentData"