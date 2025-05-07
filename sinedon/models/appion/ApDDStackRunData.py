# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class ApDDStackRunData(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    runname =  models.TextField(blank=True,null=True) 
    ref_apddstackparamsdata_params = models.IntegerField(
        db_column="REF|ApDDStackParamsData|params",
        blank=True,
        null=True,
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
    class Meta:
        managed = False
        verbose_name = "ApDDStackRunData"
        verbose_name_plural = "ApDDStackRunData"
        db_table = "ApDDStackRunData"