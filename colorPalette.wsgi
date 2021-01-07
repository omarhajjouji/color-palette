#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/colorPalette/")

from colorPalette import app as application
application.secret_key = 'color palette session'
