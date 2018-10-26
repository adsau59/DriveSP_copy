'''Drivesp Zip

Usage:
  zip.py VERSION_NAME

Options:
  -h --help    Show this screen.
'''


from docopt import docopt
args = docopt(__doc__)
import shutil
shutil.make_archive('out/DriveSP_{}_win'.format(args["VERSION_NAME"]), 'zip', 'win/')
shutil.make_archive('out/DriveSP_{}_linux'.format(args["VERSION_NAME"]), 'zip', 'linux/')
