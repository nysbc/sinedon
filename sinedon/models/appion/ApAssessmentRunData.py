# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
#from ..leginon import SessionData

class ApAssessmentRunData(models.Model):
	def_id = models.AutoField(db_column="DEF_id", primary_key=True)
	def_timestamp = models.DateTimeField(
		db_column="DEF_timestamp", auto_now_add=True
	)
	ref_sessiondata_session = models.IntegerField(
		db_column="REF|leginondata|SessionData|session",
		blank=True,
		null=True,
	)
	name = models.TextField(blank=True,null=True)
	class Meta:
		managed = False
		verbose_name = "ApAssessmentRunData"
		verbose_name_plural = "ApAssessmentRunData"
		db_table = "ApAssessmentRunData"