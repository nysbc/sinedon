# SPDX-License-Identifier: Apache-2.0
# Copyright 2025 New York Structural Biology Center

import django
import os
from configparser import ConfigParser
import MySQLdb

def setup(projectid=None, init=True):
    if projectid:
        sinedon_cfg=retrieveSinedonConfig()
        appiondb=retrieveAppionDBName(projectid, sinedon_cfg)
        if appiondb:
            os.environ["APPION_DB"]=appiondb
            if init:
                #initializeAppionDB(appiondb, sinedon_cfg)
                initializeAppionTables(appiondb, sinedon_cfg)
                apddstackparamsdata_fields={'preset' : 'text', 
                                            'align' : "tinyint(1) DEFAULT '0'",
                                            'bin' : 'int DEFAULT NULL',
                                            'REF|ApDDStackRunData|unaligned_ddstackrun' : 'int DEFAULT NULL',
                                            'REF|ApStackData|stack' : 'int DEFAULT NULL',
                                            'method' : 'text',
                                            'REF|ApDEAlignerParamsData|de_aligner' : 'int DEFAULT NULL'}
                apddstackparamsdata_keys={'REF|ApDDStackRunData|unaligned_ddstackrun'  : "KEY 'REF|ApDDStackRunData|unaligned_ddstackrun' ('REF|ApDDStackRunData|unaligned_ddstackrun')",
                                          'REF|ApStackData|stack' : "KEY 'REF|ApStackData|stack' ('REF|ApStackData|stack')",
                                          'REF|ApDEAlignerParamsData|de_aligner' : "KEY 'REF|ApDEAlignerParamsData|de_aligner' ('REF|ApDEAlignerParamsData|de_aligner')"}
                for field in apddstackparamsdata_fields.keys():
                    fieldexists=columnExists(appiondb, sinedon_cfg, "ApDDStackParamsData", field)
                    if not fieldexists:
                        columndefine=apddstackparamsdata_fields[field]
                        # Not valid SQL
                        #if field in apddstackparamsdata_keys.keys():
                        #    columndefine+=" " + apddstackparamsdata_keys[field]
                        addColumn(appiondb, sinedon_cfg, "ApDDStackParamsData", field, columndefine)
                apacerundatafields = {
                    "REF|ApAceParamsData|aceparams": "int(11) NULL",
                    "REF|ApCtfTiltParamsData|ctftilt_params": "int(11) NULL",
                    "REF|ApXmippCtfParamsData|xmipp_ctf_params": "int(11) NULL",
                    "REF|ApAce2ParamsData|ace2_params": "int(11) NULL",
                    "REF|ApCtfFind4ParamsData|ctffind4_params": "int(11) NULL",
                    "transferred": "tinyint(1) NULL",
                    "REF|ApAceTransferParamsData|transfer_params": "int(11) NULL",
                    "REF|leginondata|SessionData|session": "int(11) NULL",
                    "REF|ApPathData|path": "int(11) NULL",
                    "name": "text NULL",
                    "hidden": "tinyint(1) NULL",
                }

                for field in apacerundatafields.keys():
                    fieldexists=columnExists(appiondb, sinedon_cfg, "ApAceRunData", field)
                    if not fieldexists:
                        columndefine=apacerundatafields[field]
                        addColumn(appiondb, sinedon_cfg, "ApAceRunData", field, columndefine)

                apctfdatafields = {
                    "REF|ApAceRunData|acerun": "int(11) NULL",
                    "REF|leginondata|AcquisitionImageData|image": "int(11) NULL",
                    "cs": "double NULL",
                    "defocusinit": "double NULL",
                    "amplitude_contrast": "double NULL",
                    "defocus1": "double NULL",
                    "defocus2": "double NULL",
                    "angle_astigmatism": "double NULL",
                    "ctffind4_resolution": "double NULL",
                    "confidence": "double NULL",
                    "confidence_d": "double NULL",
                    "confidence_30_10": "double NULL",
                    "confidence_5_peak": "double NULL",
                    "overfocus_conf_30_10": "double NULL",
                    "overfocus_conf_5_peak": "double NULL",
                    "resolution_80_percent": "double NULL",
                    "resolution_50_percent": "double NULL",
                    "graph1": "text NULL",
                    "graph2": "text NULL",
                    "graph3": "text NULL",
                    "graph4": "text NULL",
                    "localplot": "text NULL",
                    "localCTFstarfile": "text NULL",
                    "ctfvalues_file": "text NULL",
                    "cross_correlation": "double NULL",
                    "tilt_angle": "double NULL",
                    "tilt_axis_angle": "double NULL",
                    "mat_file": "text NULL",
                    "extra_phase_shift": "double NULL",
                }

                for field in apctfdatafields.keys():
                    fieldexists=columnExists(appiondb, sinedon_cfg, "ApCtfData", field)
                    if not fieldexists:
                        columndefine=apctfdatafields[field]
                        addColumn(appiondb, sinedon_cfg, "ApCtfData", field, columndefine)

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
    c.close()
    db.close()
    app_db=None
    if q_resultset:
        if q_resultset[0]:
            app_db=str(q_resultset[0])
    return app_db

def columnExists(app_db, sinedon_cfg, table, column):
    """
    check if column exists
    """
    if not sinedon_cfg or not app_db or not table or not column:
        return None
    db=MySQLdb.connect(host=sinedon_cfg["global"]["host"],
                    user=sinedon_cfg["global"]["user"],
                    password=sinedon_cfg["global"]["passwd"],
                    port=3306,
                    database=app_db)
    c=db.cursor()
    c.execute("SHOW COLUMNS FROM `%s` WHERE Field='%s';" % (table, column))
    c.close()
    db.close()
    return True if int(c.rowcount) > 0 else False

def addColumn(app_db, sinedon_cfg, table, column, columndefine):
    """
    add a column to a table
    """
    if not sinedon_cfg or not app_db or not table or not column or not columndefine:
        return None
    db=MySQLdb.connect(host=sinedon_cfg["global"]["host"],
                    user=sinedon_cfg["global"]["user"],
                    password=sinedon_cfg["global"]["passwd"],
                    port=3306,
                    database=app_db)
    c=db.cursor()
    c.execute("ALTER TABLE `%s` ADD COLUMN `%s` %s;" % (table, column, columndefine))
    c.close()
    db.close()

def initializeAppionTables(app_db, sinedon_cfg):
    app_db_create_cmds = ["CREATE TABLE IF NOT EXISTS `ApAceRunData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|ApAceParamsData|aceparams` int DEFAULT NULL,  `REF|ApCtfTiltParamsData|ctftilt_params` int DEFAULT NULL,  `REF|ApAce2ParamsData|ace2_params` int DEFAULT NULL,  `REF|leginondata|SessionData|session` int DEFAULT NULL,  `REF|ApPathData|path` int DEFAULT NULL,  `name` text,  `hidden` tinyint(1) DEFAULT '0',  `REF|ApXmippCtfParamsData|xmipp_ctf_params` int DEFAULT NULL,  `REF|ApCtfFind4ParamsData|ctffind4_params` int DEFAULT NULL,  `transferred` tinyint(1) DEFAULT '0',  `REF|ApAceTransferParamsData|transfer_params` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApAceParamsData|aceparams` (`REF|ApAceParamsData|aceparams`),  KEY `REF|ApCtfTiltParamsData|ctftilt_params` (`REF|ApCtfTiltParamsData|ctftilt_params`),  KEY `REF|ApAce2ParamsData|ace2_params` (`REF|ApAce2ParamsData|ace2_params`),  KEY `REF|leginondata|SessionData|session` (`REF|leginondata|SessionData|session`),  KEY `REF|ApPathData|path` (`REF|ApPathData|path`),  KEY `hidden` (`hidden`),  KEY `REF|ApXmippCtfParamsData|xmipp_ctf_params` (`REF|ApXmippCtfParamsData|xmipp_ctf_params`),  KEY `REF|ApCtfFind4ParamsData|ctffind4_params` (`REF|ApCtfFind4ParamsData|ctffind4_params`),  KEY `REF|ApAceTransferParamsData|transfer_params` (`REF|ApAceTransferParamsData|transfer_params`))", 
                          "CREATE TABLE IF NOT EXISTS `ApAppionJobData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|ApPathData|path` int DEFAULT NULL,  `name` text,  `jobtype` text,  `REF|ApPathData|dmfpath` int DEFAULT NULL,  `REF|ApPathData|clusterpath` int DEFAULT NULL,  `REF|leginondata|SessionData|session` int DEFAULT NULL,  `cluster` text,  `clusterjobid` int DEFAULT NULL,  `status` varchar(1) DEFAULT NULL,  `user` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApPathData|clusterpath` (`REF|ApPathData|clusterpath`),  KEY `REF|leginondata|SessionData|session` (`REF|leginondata|SessionData|session`),  KEY `REF|ApPathData|dmfpath` (`REF|ApPathData|dmfpath`),  KEY `clusterjobid` (`clusterjobid`),  KEY `status` (`status`),  KEY `jobtype_10` (`jobtype`(10)))",
                          "CREATE TABLE IF NOT EXISTS `ApAssessmentData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|ApAssessmentRunData|assessmentrun` int DEFAULT NULL,  `REF|leginondata|AcquisitionImageData|image` int DEFAULT NULL,  `selectionkeep` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApAssessmentRunData|assessmentrun` (`REF|ApAssessmentRunData|assessmentrun`),  KEY `REF|leginondata|AcquisitionImageData|image` (`REF|leginondata|AcquisitionImageData|image`))", 
                          "CREATE TABLE IF NOT EXISTS `ApAssessmentRunData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|leginondata|SessionData|session` int DEFAULT NULL,  `name` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|leginondata|SessionData|session` (`REF|leginondata|SessionData|session`))", 
                          "CREATE TABLE IF NOT EXISTS `ApCtfData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|ApAceRunData|acerun` int DEFAULT NULL,  `REF|leginondata|AcquisitionImageData|image` int DEFAULT NULL,  `defocus1` double DEFAULT NULL,  `defocus2` double DEFAULT NULL,  `defocusinit` double DEFAULT NULL,  `amplitude_contrast` double DEFAULT NULL,  `angle_astigmatism` double DEFAULT NULL,  `tilt_angle` double DEFAULT NULL,  `tilt_axis_angle` double DEFAULT NULL,  `snr` double DEFAULT NULL,  `confidence` double DEFAULT NULL,  `confidence_d` double DEFAULT NULL,  `graph1` text,  `graph2` text,  `mat_file` text,  `cross_correlation` double DEFAULT NULL,  `ctfvalues_file` text,  `cs` double DEFAULT NULL,  `noise1` double DEFAULT NULL,  `noise2` double DEFAULT NULL,  `noise3` double DEFAULT NULL,  `noise4` double DEFAULT NULL,  `envelope1` double DEFAULT NULL,  `envelope2` double DEFAULT NULL,  `envelope3` double DEFAULT NULL,  `envelope4` double DEFAULT NULL,  `lowercutoff` double DEFAULT NULL,  `uppercutoff` double DEFAULT NULL,  `ctffind4_resolution` double DEFAULT NULL,  `confidence_30_10` double DEFAULT NULL,  `confidence_5_peak` double DEFAULT NULL,  `overfocus_conf_30_10` double DEFAULT NULL,  `overfocus_conf_5_peak` double DEFAULT NULL,  `resolution_80_percent` double DEFAULT NULL,  `resolution_50_percent` double DEFAULT NULL,  `graph3` text,  `graph4` text,  `localplot` text,  `localCTFstarfile` text,  `extra_phase_shift` double DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApAceRunData|acerun` (`REF|ApAceRunData|acerun`),  KEY `REF|leginondata|AcquisitionImageData|image` (`REF|leginondata|AcquisitionImageData|image`))", 
                          "CREATE TABLE IF NOT EXISTS `ApCtfFind4ParamsData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  `bestdb` tinyint(1) DEFAULT '0',  `ampcontrast` double DEFAULT NULL,  `fieldsize` int DEFAULT NULL,  `cs` double DEFAULT NULL,  `resmin` double DEFAULT NULL,  `defstep` double DEFAULT NULL,  `shift_phase` tinyint(1) DEFAULT '0',  `min_phase_shift` double DEFAULT NULL,  `max_phase_shift` double DEFAULT NULL,  `phase_search_step` double DEFAULT NULL,  `local_refine` tinyint(1) DEFAULT '0',  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`))", 
                          "CREATE TABLE IF NOT EXISTS `ApCtfTiltParamsData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `medium` text,  `ampcarbon` double DEFAULT NULL,  `ampice` double DEFAULT NULL,  `fieldsize` int DEFAULT NULL,  `cs` double DEFAULT NULL,  `bin` int DEFAULT NULL,  `resmin` double DEFAULT NULL,  `resmax` double DEFAULT NULL,  `defstep` double DEFAULT NULL,  `dast` double DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`))", 
                          "CREATE TABLE IF NOT EXISTS `ApDDAlignImagePairData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  `REF|leginondata|AcquisitionImageData|source` int DEFAULT NULL,  `REF|leginondata|AcquisitionImageData|result` int DEFAULT NULL,  `REF|ApDDStackRunData|ddstackrun` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|leginondata|AcquisitionImageData|source` (`REF|leginondata|AcquisitionImageData|source`),  KEY `REF|leginondata|AcquisitionImageData|result` (`REF|leginondata|AcquisitionImageData|result`),  KEY `REF|ApDDStackRunData|ddstackrun` (`REF|ApDDStackRunData|ddstackrun`))", 
                          "CREATE TABLE IF NOT EXISTS `ApDDAlignStatsData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  `REF|leginondata|AcquisitionImageData|image` int DEFAULT NULL,  `REF|ApDDStackRunData|ddstackrun` int DEFAULT NULL,  `REF|ApDDFrameTrajectoryData|trajectory` int DEFAULT NULL,  `apix` double DEFAULT NULL,  `top_shift1_value` double DEFAULT NULL,  `top_shift2_value` double DEFAULT NULL,  `top_shift3_value` double DEFAULT NULL,  `top_shift1_index` int DEFAULT NULL,  `top_shift2_index` int DEFAULT NULL,  `top_shift3_index` int DEFAULT NULL,  `median_shift_value` double DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|leginondata|AcquisitionImageData|image` (`REF|leginondata|AcquisitionImageData|image`),  KEY `REF|ApDDStackRunData|ddstackrun` (`REF|ApDDStackRunData|ddstackrun`),  KEY `REF|ApDDFrameTrajectoryData|trajectory` (`REF|ApDDFrameTrajectoryData|trajectory`))", 
                          "CREATE TABLE IF NOT EXISTS `ApDDFrameTrajectoryData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  `REF|leginondata|AcquisitionImageData|image` int DEFAULT NULL,  `REF|ApStackParticleData|particle` int DEFAULT NULL,  `REF|ApDDStackRunData|ddstackrun` int DEFAULT NULL,  `SEQ|pos_x` text,  `SEQ|pos_y` text,  `last_x` double DEFAULT NULL,  `last_y` double DEFAULT NULL,  `number_of_positions` int DEFAULT NULL,  `reference_index` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|leginondata|AcquisitionImageData|image` (`REF|leginondata|AcquisitionImageData|image`),  KEY `REF|ApStackParticleData|particle` (`REF|ApStackParticleData|particle`),  KEY `REF|ApDDStackRunData|ddstackrun` (`REF|ApDDStackRunData|ddstackrun`))", 
                          "CREATE TABLE IF NOT EXISTS `ApDDStackParamsData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `preset` text,  `align` tinyint(1) DEFAULT '0',  `bin` int DEFAULT NULL,  `REF|ApDDStackRunData|unaligned_ddstackrun` int DEFAULT NULL,  `REF|ApStackData|stack` int DEFAULT NULL,  `method` text,  `REF|ApDEAlignerParamsData|de_aligner` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApDDStackRunData|unaligned_ddstackrun` (`REF|ApDDStackRunData|unaligned_ddstackrun`),  KEY `REF|ApStackData|stack` (`REF|ApStackData|stack`),  KEY `REF|ApDEAlignerParamsData|de_aligner` (`REF|ApDEAlignerParamsData|de_aligner`))", 
                          "CREATE TABLE IF NOT EXISTS `ApDDStackRunData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `runname` text,  `REF|ApDDStackParamsData|params` int DEFAULT NULL,  `REF|leginondata|SessionData|session` int DEFAULT NULL,  `REF|ApPathData|path` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApDDStackParamsData|params` (`REF|ApDDStackParamsData|params`),  KEY `REF|leginondata|SessionData|session` (`REF|leginondata|SessionData|session`),  KEY `REF|ApPathData|path` (`REF|ApPathData|path`))", 
                          "CREATE TABLE IF NOT EXISTS `ApPathData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `path` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `path_index32` (`path`(32)))", 
                          "CREATE TABLE IF NOT EXISTS `ApStackData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `REF|ApPathData|path` int DEFAULT NULL,  `name` text,  `description` text,  `hidden` tinyint(1) DEFAULT '0',  `REF|ApStackData|oldstack` int DEFAULT NULL,  `substackname` text,  `pixelsize` double DEFAULT NULL,  `centered` tinyint(1) DEFAULT '0',  `junksorted` tinyint(1) DEFAULT '0',  `beamtilt_corrected` tinyint(1) DEFAULT '0',  `mask` int DEFAULT NULL,  `maxshift` int DEFAULT NULL,  `boxsize` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ApPathData|path` (`REF|ApPathData|path`),  KEY `hidden` (`hidden`),  KEY `REF|ApStackData|oldstack` (`REF|ApStackData|oldstack`),  KEY `centered` (`centered`),  KEY `junksorted` (`junksorted`),  KEY `beamtilt_corrected` (`beamtilt_corrected`))", 
                          "CREATE TABLE IF NOT EXISTS `ApSymmetryData` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `eman_name` varchar(8) DEFAULT NULL,  `fold_symmetry` int DEFAULT NULL,  `symmetry` text,  `description` text,  PRIMARY KEY (`DEF_id`),  UNIQUE KEY `symmetry` (`symmetry`(12)),  KEY `eman_name` (`eman_name`),  KEY `DEF_timestamp` (`DEF_timestamp`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptHostName` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `name` text,  `ip` text,  `system` text,  `distro` text,  `arch` text,  `nproc` int DEFAULT NULL,  `memory` int DEFAULT NULL,  `cpu_vendor` text,  `gpu_vendor` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptParamName` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `name` text,  `REF|ScriptProgramName|progname` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ScriptProgramName|progname` (`REF|ScriptProgramName|progname`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptParamValue` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `value` text,  `usage` text,  `REF|ScriptParamName|paramname` int DEFAULT NULL,  `REF|ScriptProgramRun|progrun` int DEFAULT NULL,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ScriptParamName|paramname` (`REF|ScriptParamName|paramname`),  KEY `REF|ScriptProgramRun|progrun` (`REF|ScriptProgramRun|progrun`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptProgramName` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `name` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptProgramRun` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `runname` text,  `revision` text,  `REF|ScriptProgramName|progname` int DEFAULT NULL,  `REF|ScriptUserName|username` int DEFAULT NULL,  `REF|ScriptHostName|hostname` int DEFAULT NULL,  `REF|ApPathData|rundir` int DEFAULT NULL,  `REF|ApAppionJobData|job` int DEFAULT NULL,  `REF|ApPathData|appion_path` int DEFAULT NULL,  `unixshell` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`),  KEY `REF|ScriptProgramName|progname` (`REF|ScriptProgramName|progname`),  KEY `REF|ScriptUserName|username` (`REF|ScriptUserName|username`),  KEY `REF|ScriptHostName|hostname` (`REF|ScriptHostName|hostname`),  KEY `REF|ApPathData|rundir` (`REF|ApPathData|rundir`),  KEY `REF|ApAppionJobData|job` (`REF|ApAppionJobData|job`),  KEY `REF|ApPathData|appion_path` (`REF|ApPathData|appion_path`))", 
                          "CREATE TABLE IF NOT EXISTS `ScriptUserName` (  `DEF_id` int NOT NULL AUTO_INCREMENT,  `DEF_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `name` text,  `uid` int DEFAULT NULL,  `gid` int DEFAULT NULL,  `fullname` text,  PRIMARY KEY (`DEF_id`),  KEY `DEF_timestamp` (`DEF_timestamp`))"]
    db=MySQLdb.connect(host=sinedon_cfg["global"]["host"],
                    user=sinedon_cfg["global"]["user"],
                    password=sinedon_cfg["global"]["passwd"],
                    port=3306,
                    database=app_db)
    c=db.cursor()
    for cmd in app_db_create_cmds:
        c.execute(cmd)
    c.close()
    db.close()

def initializeAppionDB(app_db, sinedon_cfg):
    db=MySQLdb.connect(host=sinedon_cfg["global"]["host"],
                    user=sinedon_cfg["global"]["user"],
                    password=sinedon_cfg["global"]["passwd"],
                    port=3306)
    c=db.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS %s" % app_db)
    c.close()
    db.close()

def retrieveSecretKey():
    if "SINEDON_SECRET_KEY" not in os.environ.keys():
        raise RuntimeError("SINEDON_SECRET_KEY is not defined as an environment variable.")
    return os.environ["SINEDON_SECRET_KEY"]

def retrieveSinedonConfig():
    if "SINEDON_CFG_PATH" not in os.environ.keys():
        if "HOME" in os.environ.keys():
            SINEDON_CFG_PATH=os.environ["HOME"]
        else:
            raise RuntimeError("SINEDON_CFG_PATH not defined as an environment variable and could not determine path to home directory.")
    else:
        SINEDON_CFG_PATH=os.environ["SINEDON_CFG_PATH"]
        
    SINEDON_PATH=os.path.join(SINEDON_CFG_PATH,"sinedon.cfg")
    if not os.path.exists(SINEDON_PATH):
        raise FileExistsError("Sinedon configuration file at %s does not exist." % SINEDON_PATH)
    SINEDON_CFG = ConfigParser()
    if not SINEDON_CFG.read(SINEDON_PATH):
        raise RuntimeError("Unable to read Sinedon configuration file at %s" % os.path.join(SINEDON_CFG_PATH,"sinedon.cfg"))
    return SINEDON_CFG

def retrieveAppionDB():
    if "APPION_DB" not in os.environ.keys():
        return None
    return os.environ["APPION_DB"]
