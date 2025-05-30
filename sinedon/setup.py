# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

import django
import os
from configparser import ConfigParser
import MySQLdb

def setup(projectid=None):
    if projectid:
        sinedon_cfg=retrieveSinedonConfig()
        appiondb=retrieveAppionDBName(projectid, sinedon_cfg)
        if appiondb:
            os.environ["APPION_DB"]=appiondb
    django.setup()

# Appion database is initialized by myamiweb / web viewer.
def retrieveAppionDBName(projectid, sinedon_cfg):
    if not projectid or not sinedon_cfg:
        return None
    db=MySQLdb.connect(host=sinedon_cfg["global"]["host"],
                       user=sinedon_cfg["global"]["user"],
                       password=sinedon_cfg["global"]["passwd"],
                       port=3306,
                       database=sinedon_cfg["projectdata"]["db"])
    c=db.cursor()
    c.execute("""SELECT appiondb FROM processingdb WHERE `REF|projects|project`='%s'""" % (projectid,))
    q_resultset=c.fetchone()
    app_db=None
    if q_resultset:
        if q_resultset[0]:
            app_db=str(q_resultset[0])
    return app_db

def retrieveSecretKey():
    if "SINEDON_SECRET_KEY" not in os.environ.keys():
        raise RuntimeError("SINEDON_SECRET_KEY is not defined as an environment variable.")
    return os.environ["SINEDON_SECRET_KEY"]

def retrieveSinedonConfig():
    if "SINEDON_CFG_PATH" not in os.environ.keys():
        raise RuntimeError("SINEDON_CFG_PATH is not defined as an environment variable.")
    SINEDON_CFG_PATH=os.environ["SINEDON_CFG_PATH"]
        
    SINEDON_CFG = ConfigParser()
    if not SINEDON_CFG.read(os.path.join(SINEDON_CFG_PATH,"sinedon.cfg")):
        raise RuntimeError("Unable to read Sinedon configuration file at %s" % os.path.join(SINEDON_CFG_PATH,"sinedon.cfg"))
    return SINEDON_CFG

def retrieveAppionDB():
    if "APPION_DB" not in os.environ.keys():
        return None
    return os.environ["APPION_DB"]