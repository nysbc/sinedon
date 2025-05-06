# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

from django.db import models
#from .ScriptParamName import ScriptParamName
#from .ScriptProgramRun import ScriptProgramRun

class ScriptParamValue(models.Model):
	def_id = models.AutoField(db_column="DEF_id", primary_key=True)
	def_timestamp = models.DateTimeField(
		db_column="DEF_timestamp", auto_now_add=True
	)

	value = models.TextField(blank=True,null=True)
	usage = models.TextField(blank=True,null=True)
	ref_scriptparamname_paramname = models.IntegerField(
		db_column="REF|ScriptParamName|paramname",
		blank=True,
		null=True,
	)
	ref_scriptprogramrun_progrun = models.IntegerField(
		db_column="REF|ScriptProgramRun|progrun",
		blank=True,
		null=True,
	)

	class Meta:
		managed = False
		verbose_name = "ScriptParamValue"
		verbose_name_plural = "ScriptParamValue"
		db_table = "ScriptParamValue"