# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
from .projects import projects

class processingdb(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )
    ref_projects_project = models.ForeignKey(
        projects,
        db_column="REF|projects|project",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
    appiondb = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        verbose_name = "processingdb"
        verbose_name_plural = "processingdb"
        db_table = "processingdb"