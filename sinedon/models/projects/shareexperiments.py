# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class shareexperiments(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )	
    ref_userdata_user = models.IntegerField(db_column="REF|leginondata|UserData|user", blank=True, null=True)
    ref_sessiondata_session = models.IntegerField(db_column="REF|leginondata|SessionData|session", blank=True, null=True)
    class Meta:
        managed = False
        verbose_name = "shareexperiments"
        verbose_name_plural = "shareexperiments"
        db_table = "shareexperiments"