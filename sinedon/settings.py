# SPDX-License-Identifier: Apache-2.0
# Copyright 2024-2025 New York Structural Biology Center

import os
from .setup import retrieveSecretKey, retrieveSinedonConfig, retrieveAppionDB

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = retrieveSecretKey()

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

SINEDON_CFG = retrieveSinedonConfig()

APPION_DB = retrieveAppionDB()

try:
    DATABASES = {
        "leginon": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": SINEDON_CFG["leginondata"]["db"],
            "USER": SINEDON_CFG["global"]["user"],
            "PASSWORD": SINEDON_CFG["global"]["passwd"],
            "HOST": SINEDON_CFG["global"]["host"],
            "PORT": "3306",
            "ATOMIC_REQUESTS": True,
        },
        "projects": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": SINEDON_CFG["projectdata"]["db"],
            "USER": SINEDON_CFG["global"]["user"],
            "PASSWORD": SINEDON_CFG["global"]["passwd"],
            "HOST": SINEDON_CFG["global"]["host"],
            "PORT": "3306",
            "ATOMIC_REQUESTS": True,
        },
    }
    DATABASES["default"] = DATABASES["leginon"]
    DATABASE_ROUTERS=["sinedon.routers.leginon.LeginonDBRouter", "sinedon.routers.projects.ProjectDBRouter"]
    if APPION_DB:
        DATABASES["appion"] = {
            "ENGINE": "django.db.backends.mysql",
            "NAME": APPION_DB,
            "USER": SINEDON_CFG["global"]["user"],
            "PASSWORD": SINEDON_CFG["global"]["passwd"],
            "HOST": SINEDON_CFG["global"]["host"],
            "PORT": "3306",
            "ATOMIC_REQUESTS": True,
        }
        DATABASE_ROUTERS.append("sinedon.routers.appion.AppionDBRouter")
except KeyError as e:
    raise RuntimeError("Sinedon Configuration does not define necessary fields.") from e

INSTALLED_APPS = ("sinedon",)