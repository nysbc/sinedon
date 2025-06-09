# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

class AppionDBRouter:
    appiondb_db_tables = ["ApAceRunData",
                          "ApAppionJobData",
                          "ApAssessmentRunData",
                          "ApCtfData",
                          "ApCtfFind4ParamsData",
                          "ApCtfTiltParamsData",
                          "ApDDAlignImagePairData",
                          "ApDDAlignStatsData",
                          "ApDDFrameTrajectoryData",
                          "ApDDStackParamsData",
                          "ApDDStackRunData",
                          "ApPathData",
                          "ApStackData",
                          "ApSymmetryData",
                          "cryosparc",
                          "poster",
                          "ScriptHostName",
                          "ScriptParamName",
                          "ScriptParamValue",
                          "ScriptProgramName",
                          "ScriptProgramRun",
                          "ScriptUserName"]
    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.appiondb_db_tables:
            return "appion"
        return None
    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.appiondb_db_tables:
            return "appion"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.db_table in self.appiondb_db_tables
            or obj2._meta.db_table in self.appiondb_db_tables
        ):
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None