import json
import os
__title__ = 'safety-db'
__version__ = '2019.5.5'
__author__ = 'Justin Womersley <support@pyup.io>'
__copyright__ = '2016-2017 PyUp'
__license__ = 'Attribution-NonCommercial-ShareAlike 4.0 International'
__all__ = (
    'INSECURE',
    'INSECURE_FULL',
)

# Set default values in case there is an issue loading the data files.
INSECURE = []
INSECURE_FULL = []

try:
    # Get the data files from the package using pkg_resources so the package is zip safe
    import pkg_resources
    INSECURE = json.loads(pkg_resources.resource_string("safety_db", "data/insecure.json").decode(errors='ignore'))
    INSECURE_FULL = json.loads(pkg_resources.resource_string("safety_db", "data/insecure_full.json").decode(errors='ignore'))
except ImportError:
    # Fallback to attempting to load the data files from the filesystem.  This is needed because the setup.py
    # file imports this module before the package is created.  So the data files won't be accesible using pkg_resources
    # and generating an exception will break package creation.
    __data_dir = os.path.dirname(__file__)
    with open(os.path.join(__data_dir, "data/insecure.json")) as __f:
        try:
            INSECURE = json.loads(__f.read())
        except ValueError as e:
            pass

    with open(os.path.join(__data_dir, "data/insecure_full.json")) as __f:
        try:
            INSECURE_FULL = json.loads(__f.read())
        except ValueError as e:
             pass
