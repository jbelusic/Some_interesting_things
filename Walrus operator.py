
#Walrus operator :=

import os

def _getuserbase():
    env_base = os.environ.get("PYTHONUSERBASE", None)
    if env_base:
        return env_base
#== same as
def _getuserbase():
    if env_base := os.environ.get("PYTHONUSERBASE", None):
        return env_base
