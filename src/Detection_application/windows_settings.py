#Still under devolpment!

import subprocess
import winreg
import win32api

ADVANCED_PATH = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
VISUAL_EFFECTS = {
    "taskbar_animations": [
    r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
    "TaskbarAnimations",
    None
    ],
    "drag_full_windows": [
    r"Control Panel\Desktop",
    "DragFullWindows",
    None
    ],
    "window_drop_shadow": [
    r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
    "DropShadow",
    None
    ],
    "listview_alpha_select": [
    r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",
    "ListviewAlphaSelect",
    None
    ],
    "font_smoothing": [
    r"Control Panel\Desktop",
    "FontSmoothing",
    None
    ]
}



def read_registry_dword(path, name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, path) as key:
            value, regtype = winreg.QueryValueEx(key, name)
            if regtype == winreg.REG_DWORD:
                return int(value)
    except FileNotFoundError:
        return None
    except OSError:
        return None
    return None



def gamemode():
    # Check if game mode is on
    cmd = r'reg query "HKCU\Software\Microsoft\GameBar" /v AutoGameModeEnabled'
    result = subprocess.check_output(cmd, shell=True, text=True)
    if result.find('0x0') != -1:
        return False   
    elif result.find('0x1')  != -1:
        return True
    else:
        return None



def refresh_rate():
    device = win32api.EnumDisplayDevices()
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, 'DisplayFrequency')


def animations(visual_effects: dict):
    settings = {}
    for key in visual_effects:
        visual_effects[key][2]= read_registry_dword(visual_effects[key][0], visual_effects[key][1])
    
    for data in visual_effects.items():
        if data[1][2] != None:
            settings[data[0]] = data[1]

    return settings

