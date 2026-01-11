import subprocess
from Windows_settings import read_registry_dword as dw


def get_list():
    cmd = "powercfg /list"
    try:
        output = subprocess.check_output(cmd, shell=True, text=True)
        lines = output.splitlines()

        return [
            line for line in lines
            if "Power Scheme GUID:" in line
        ]

    except subprocess.CalledProcessError:
        return False


def active_powerplan():
    power_list = get_list()
    if not power_list:
        return False

    for power in power_list:
        if power.endswith("*"):
            active = power.split('(')[1][:-3]
            key = power.split()[3]

            return {
                'active': active,
                'key': key
            }

    return False


def min_proc_state():
    cmd = 'powercfg /query SCHEME_CURRENT SUB_PROCESSOR'
    try:
        output = subprocess.check_output(cmd, shell=True, text=True)
        lines = output.splitlines()

        setting_lines = [
            line for line in lines
            if "Power Setting Index" in line
        ][:-2]

        values = []
        for line in setting_lines:
            hex_value = line.split()[-1][2:]
            values.append(int(hex_value, 16))

        return {
            'battery_min_proc': values[0],
            'plug_min_proc': values[1]
        }

    except subprocess.CalledProcessError:
        return False


def core_parking():
    PATH = r'\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings'
    NAME_KEY = 'ValueMax'

    try:
        return {
            'core_parking_value': dw(PATH, NAME_KEY)
        }
    except Exception:
        return False


def proc_boost():
    cmd = 'powercfg /qh SCHEME_CURRENT SUB_PROCESSOR be337238-0d82-4146-a960-4f3749d470c7'
    boost_modes = {
        0: "Disabled (Gedeactiveerd)",
        1: "Enabled (Ingeschakeld)",
        2: "Aggressive (Agressief)",
        3: "Efficient Enabled (Efficiënt Ingeschakeld)",
        4: "Efficient Aggressive (Efficiënt Agressief)",
        5: "Aggressive At Guaranteed (Agressief bij gegarandeerde klok)",
        6: "Efficient Aggressive At Guaranteed (Efficiënt Agressief bij gegarandeerde klok)"
    }

    output = subprocess.check_output(cmd, shell=True, text=True)
    lines = output.splitlines()[-4:-2]

    res = []
    for line in lines:
        value = int(line.split()[line.split().index('Index:') + 1][3:], 16)
        res.extend([value, boost_modes.get(value, "Onbekende modus")])

    return {
        'battery_boost_mode': res[0],
        'battery_boost_mode_name': res[1],
        'plugged_in_boost_mode': res[2],
        'plugged_in_boost_mode_name': res[3]
    }


def main():
    data = active_powerplan()
    if data:
        print(f"Active powerplan: {data['active']} - {data['key']}")

    data = min_proc_state()
    if data:
        print(f"Minimum processing power on battery: {data['battery_min_proc']}%")
        print(f"Minimum processing power plugged in: {data['plug_min_proc']}%")

    data = core_parking()
    if data:
        print(f"Core parking percent: {data['core_parking_value']}%")

    data = proc_boost()
    if data:
        print(f"Battery CPU boost mode: {data['battery_boost_mode_name']}")
        print(f"Plugged in CPU boost mode: {data['plugged_in_boost_mode_name']}")


if __name__ == "__main__":
    main()
