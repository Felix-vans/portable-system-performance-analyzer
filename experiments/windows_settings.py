# still in devolpmemnt!

import subprocess


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
    cmd = "powercfg /list"
    output = subprocess.check_output(cmd, shell=True, text=True)
    if output.find("e9a42b02-d5df-448d-aa00-03f14749eb61") == -1:
        return False
    else:
        return True


def performance_options():
    ListViewAlphaSelect = subprocess.check_output("")

    pass
"""
HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
  ListviewAlphaSelect = 0
  ListviewShadow = 0
  TaskbarAnimations = 0
  EnableAeroPeek = 0

HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects
  VisualFXSetting = 3

"""

