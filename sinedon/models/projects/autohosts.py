# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class autohosts(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )	
    hostname = models.TextField(blank=True, null=True)		
    appion_wrapper = models.TextField(blank=True, null=True)		
    ddalign_gpus = models.TextField(db_column="SEQ|ddalign_gpus",blank=True, null=True)		
    loop_max	= models.IntegerField(blank=True, null=True)		
    class Meta:
        managed = False
        verbose_name = "autohosts"
        verbose_name_plural = "autohosts"
        db_table = "autohosts"