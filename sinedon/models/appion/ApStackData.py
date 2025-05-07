# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York models.TextField(blank=True,null=True)uctural Biology Center

from django.db import models

class ApStackData(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    path = models.IntegerField(blank=True,null=True)
    name = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    hidden = models.BooleanField(blank=True,null=True)
    oldstack = models.IntegerField(blank=True,null=True)
    substackname = models.TextField(blank=True,null=True)
    pixelsize = models.FloatField(blank=True,null=True)
    centered = models.BooleanField(blank=True,null=True)
    radial_averaged = models.BooleanField(blank=True,null=True)
    junksorted = models.BooleanField(blank=True,null=True)
    beamtilt_corrected = models.BooleanField(blank=True,null=True)
    mask = int
    maxshift = int
    boxsize = int
    class Meta:
        managed = False
        verbose_name = "ApStackData"
        verbose_name_plural = "ApStackData"
        db_table = "ApStackData"