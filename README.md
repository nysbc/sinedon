# SEMC Sinedon

## Overview

SEMC Sinedon is a reimplementation of the Leginon Cryo-EM suite's Sinedon library (classic Sinedon).
Classic Sinedon is a full-fledged object-relational mapping (ORM) package written in Python.
SEMC Sinedon differs from classic Sinedon in that it only implements the data model used by Appion and Leginon,
and delegates ORM functionality to Django.  The reason for creating this version of Sinedon is to
reduce the scope of what is maintained by the research computing staff at the Simons Electron Microscopy Center (SEMC).
Phrased differently, we strove to reduce the maintenance burden of our primary data pipeline.

## Installation

SEMC Sinedon requires [poetry](https://python-poetry.org/docs/).  After installing poetry, SEMC Sinedon may be installed by
running the following command in a cloned copy of this repository:

```
poetry install
```

## Configuration File

SEMC Sinedon retrieves database connection parameters from the same configuration
file used by classic Sinedon  (`sinedon.cfg`). The `SINEDON_CFG_PATH` shell
environment variable should be defined so that SEMC Sinedon knows where to find this
configuration file.  If this is variable is not defined, SEMC Sinedon will try to find
`sinedon.cfg` in the current user's home directory.

## Developers Guide

### Adding a new database model/table to sinedon.

1. Create the model in a new file under the appropriate location (e.g., `models/appion` for Appion DB tables, `models/leginon` for Leginon DB tables)
2. Ensure that the Django `Meta` class is defined and that `db_table` is set.
3. Add the model to the `__init__.py` file under `models/{appion,leginon,projects}`.
4. Add the table name to the list of database table names in the appropriate router class under `routers/{appion,leginon,projects}`.