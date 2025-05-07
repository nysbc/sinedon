# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class ApAppionJobData(models.Model):
	def_id = models.AutoField(db_column="DEF_id", primary_key=True)
	def_timestamp = models.DateTimeField(
		db_column="DEF_timestamp", auto_now_add=True
	)
	ref_appathdata_path = models.IntegerField(
		db_column="REF|ApPathData|path",
		blank=True,
		null=True,
	)
	ref_sessiondata_session = models.IntegerField(
		db_column="REF|SessionData|session",
		blank=True,
		null=True,
	)
	ref_appathdata_dmfpath = models.IntegerField(
		db_column="REF|ApPathData|dmfpath",
		blank=True,
		null=True,
	)
	ref_appathdata_clusterpath= models.IntegerField(
		db_column="REF|ApPathData|clusterpath",
		blank=True,
		null=True,
	)
	name = models.TextField(blank=True,null=True)
	cluster = models.TextField(blank=True,null=True)
	jobtype = models.TextField(blank=True,null=True)
	status = models.TextField(blank=True,null=True)
	user = models.TextField(blank=True,null=True)
	clusterjobid = models.IntegerField(blank=True,null=True)
	class Meta:
		managed = False
		verbose_name = "ApAppionJobData"
		verbose_name_plural = "ApAppionJobData"
		db_table = "ApAppionJobData"