# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
#from .ScriptProgramName import ScriptProgramName

class ScriptParamName(models.Model):
	def_id = models.AutoField(db_column="DEF_id", primary_key=True)
	def_timestamp = models.DateTimeField(
		db_column="DEF_timestamp", auto_now_add=True
	)
	name = models.TextField(blank=True,null=True)
	ref_scriptprogramname_progname = models.IntegerField(
		db_column="REF|ScriptProgramName|progname",
		blank=True,
		null=True,
	)
	class Meta:
		managed = False
		verbose_name = "ScriptParamName"
		verbose_name_plural = "ScriptParamName"
		db_table = "ScriptParamName"