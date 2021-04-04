"""
    Plugin to reset osmc user password
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import time

# plugin constants
__plugin__ = "Reset osmc user password "
__author__ = "tomdoyle87
__url__ = "https://osmc.tv/"
__git_url__ = "https://github.com/tomdoyle87/osmc-password-reset"
__credits__ = "tomdoyle87"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_pw_reset')

os.system("/bin/echo -e 'osmc\nosmc' | /usr/bin/sudo /usr/bin/passwd ")
time.sleep(5)
dialog.ok("Password reset", "Now the password for osmc has been reset.")
