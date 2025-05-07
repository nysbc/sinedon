# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class ApDDStackParamsData(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    preset = models.TextField(blank=True,null=True)
    align = models.BooleanField(blank=True,null=True)
    bin = models.IntegerField(blank=True,null=True)
    ref_apddstackrundata_unaligned_ddstackrun = models.IntegerField(
        db_column="REF|ApDDStackRunData|unaligned_ddstackrun",
        blank=True,
        null=True,
    )
    ref_apstackdata_stack = models.IntegerField(
        db_column="REF|ApStackData|stack",
        blank=True,
        null=True,
    )
    method = models.TextField(blank=True,null=True)
    ref_apdealignerparamsdata_de_aligner = models.IntegerField(
        db_column="REF|ApDEAlignerParamsData|de_aligner",
        blank=True,
        null=True
    )
    class Meta:
        managed = False
        verbose_name = "ApDDStackParamsData"
        verbose_name_plural = "ApDDStackParamsData"
        db_table = "ApDDStackParamsData"