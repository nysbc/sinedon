# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class projects(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    name = models.CharField(max_length=255, blank=True, null=True)	
    short_description = models.TextField(blank=True, null=True)		
    long_description = models.TextField(blank=True, null=True)		
    category = models.TextField(blank=True, null=True)		
    funding	= models.TextField(blank=True, null=True)		
    leginondb = models.CharField(max_length=50, blank=True, null=True)		
    hidden = models.BooleanField(blank=True, null=True)	
    class Meta:
        managed = False
        verbose_name = "projects"
        verbose_name_plural = "projects"
        db_table = "projects"