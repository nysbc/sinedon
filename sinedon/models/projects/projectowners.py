# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
from .projects import projects

class projectowners(models.Model):
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
    ref_userdata_user = models.IntegerField(db_column="REF|leginondata|UserData|user", blank=True, null=True)
    class Meta:
        managed = False
        verbose_name = "projectowners"
        verbose_name_plural = "projectowners"
        db_table = "projectowners"