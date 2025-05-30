# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center
    
class ProjectDBRouter:
    project_db_tables = ["processingdb","projects"]
    def db_for_read(self, model, **hints):
        if model._meta.db_table in self.project_db_tables:
            return "projects"
        return None
    def db_for_write(self, model, **hints):
        if model._meta.db_table in self.project_db_tables:
            return "projects"
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1.model._meta.db_table in self.project_db_tables
            or obj2.model._meta.db_table in self.project_db_tables
        ):
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
