# SPDX-License-Identifier: Apache-2.0
# Copyright 2024-2025 New York Structural Biology Center

import os
from configparser import ConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if "SINEDON_SECRET_KEY" not in os.environ.keys():
    raise RuntimeError("SINEDON_SECRET_KEY is not defined as an environment variable.")
SECRET_KEY=os.environ["SINEDON_SECRET_KEY"]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

if "SINEDON_CFG_PATH" not in os.environ.keys():
    raise RuntimeError("SINEDON_CFG_PATH is not defined as an environment variable.")
SINEDON_CFG_PATH=os.environ["SINEDON_CFG_PATH"]
    
SINEDON_CFG = ConfigParser()
try:
    SINEDON_CFG.read(os.path.join(SINEDON_CFG_PATH,"sinedon.cfg"))
except Exception as e:
    raise RuntimeError("Unable to read Sinedon configuration file at %s" % os.path.join(SINEDON_CFG_PATH,"sinedon.cfg")) from e

try:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": SINEDON_CFG["leginondata"]["db"],
            "USER": SINEDON_CFG["global"]["user"],
            "PASSWORD": SINEDON_CFG["global"]["passwd"],
            "HOST": SINEDON_CFG["global"]["host"],
            "PORT": "3306",
            "ATOMIC_REQUESTS": True,
        },
    }
except KeyError as e:
    raise RuntimeError("Sinedon Configuration does not define necessary fields.") from e

INSTALLED_APPS = ("sinedon",)