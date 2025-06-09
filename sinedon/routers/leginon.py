# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

class LeginonDBRouter:
    leginon_db_tables = ["AcquisitionImageData",
                         "CameraEMData",
                         "CorrectorPlanData",
                         "InstrumentData",
                         "ObjIceThicknessData",
                         "PixelSizeCalibrationData",
                         "PresetData",
                         "ScopeEMData",
                         "SessionData",
                         "UserData",
                         "ZeroLossIceThicknessData"]
    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.leginon_db_tables:
            return "leginon"
        return None
    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.leginon_db_tables:
            return "leginon"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.db_table in self.leginon_db_tables
            or obj2._meta.db_table in self.leginon_db_tables
        ):
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None