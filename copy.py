"""Drivesp Copy

Usage:
  drivesp_copy.py PUBLISHER_PATH UPDATER_PATH_WIN UPDATER_PATH_LINUX OUT_FOLDER_NAME

Options:
  -h --help     Show this screen.
"""

from docopt import docopt
import os

args = docopt(__doc__)

from distutils.dir_util import copy_tree
from shutil import copy2

dirname = os.path.dirname(__file__)
destPub = os.path.join(dirname, args["OUT_FOLDER_NAME"]+"\\")
destUpdateWin = os.path.join(dirname, args["OUT_FOLDER_NAME"]+"\\updater\\win\\.updater\\")
destUpdateLinux = os.path.join(dirname, args["OUT_FOLDER_NAME"]+"\\updater\\linux\\.updater\\")

copy_tree(args["PUBLISHER_PATH"], destPub)
copy_tree(args["UPDATER_PATH_WIN"], destUpdateWin)
copy_tree(args["UPDATER_PATH_LINUX"], destUpdateLinux)

copy2("scripts/update.bat", os.path.join(dirname, args["OUT_FOLDER_NAME"]+"\\updater\\win\\"))
copy2("scripts/install_instruction_readme.txt", os.path.join(dirname, args["OUT_FOLDER_NAME"]+"\\updater\\linux\\"))
