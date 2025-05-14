import django
import os

def setup(db=None):
    if db:
        os.environ["SINEDON_DB_OVERRIDE"]=db
    django.setup()