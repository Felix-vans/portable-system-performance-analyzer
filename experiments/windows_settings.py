
# still in devolpmemnt!

import subprocess
import winreg

ADVANCED_PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"

SETTINGS = {
    "ListviewAlphaSelect": 0,
    "ListviewShadow": 0,
    "TaskbarAnimations": 0,
    "EnableAeroPeek": 0,
}


"""
Settings to update: 
1. Gamemode on
2. graphic optimazation
3. Disable core isolation
4 . ultimate powerplan
5. notifications off, do not disturb on
6. Apps share across devices off
7. Performance options
"""

def gamemode():
    # Check if game mode is on
    cmd = r'reg query "HKCU\Software\Microsoft\GameBar" /v AutoGameModeEnabled'
    result = subprocess.check_output(cmd, shell=True, text=True)
    if result.find('0x0') != -1:
        return False   
    elif result.find('0x1')  != -1:
        return True
    else:
        return 'Error'


def ultimate_powerplan():
    cmd_1 = "powercfg /list"
    cmd_2 = "powercfg /getactivescheme"
    ultimate_powerplan_key = "e9a42b02-d5df-448d-aa00-03f14749eb61"
    output = subprocess.check_output(cmd_1, shell=True, text=True)
    if output.find(ultimate_powerplan_key) == -1:
        exists = False
    else:
        exists = True
    if exists:
		output = subprocess.check_output(cmd_2, shell=True, text=True)
		if output.find(ultimate_powerplan_key) == -1:
			return 1, 0 #exists but not turned on
		elif output.find(ultimate_powerplan_key):
			return 1, 1 #exists and turned on
	else:
		return 0, 0 #doens't exist



def read_registry_dword(path, name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, path) as key:
            value, regtype = winreg.QueryValueEx(key, name)
            if regtype == winreg.REG_DWORD:
                return int(value)
    except FileNotFoundError:
        return 0
    except OSError:
        return 0
    return 0

results = {}

for setting in SETTINGS:
    results[setting] = read_registry_dword(ADVANCED_PATH, setting)

print(results)

"""
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
  ListviewAlphaSelect = 0
  ListviewShadow = 0
  TaskbarAnimations = 0
  EnableAeroPeek = 0

HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects
  VisualFXSetting = 3

"""

