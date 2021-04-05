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
import random
import string

# plugin constants
__plugin__ = "Reset osmc user password "
__author__ = "tomdoyle87"
__url__ = "https://osmc.tv/"
__git_url__ = "https://github.com/tomdoyle87/osmc-password-reset"
__credits__ = "tomdoyle87"
__version__ = "0.0.1"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.OSMC_pw_reset')

dialog = xbmcgui.Dialog() 
if dialog.yesno('Kodi', 'Do you want to factory reset the osmc password? If not behind a nat or you have port forwarded ssh, please select no. A random password will be set instead.'):
    Osmc = "osmc"
else:
    source = string.ascii_letters + string.digits
    Osmc = ''.join((random.choice(source) for i in range(8)))


os.system("/bin/echo -e 'osmc\nosmc' | /usr/bin/sudo /usr/bin/passwd %s"%Osmc)
time.sleep(5)
dialog.ok("Password reset", "Now the password for osmc has been reset to: " Osmc)
