# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models

class userdetails(models.Model):
    def_id = models.AutoField(db_column="DEF_id", primary_key=True)
    def_timestamp = models.DateTimeField(
        db_column="DEF_timestamp", auto_now_add=True
    )	
    ref_userdata_user = models.IntegerField(db_column="REF|leginondata|UserData|user", blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    institution = models.TextField(blank=True, null=True)
    dept = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    statecountry = models.TextField(blank=True, null=True)
    zip_code = models.TextField(db_column="zip", blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    fax = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        verbose_name = "userdetails"
        verbose_name_plural = "userdetails"
        db_table = "userdetails"