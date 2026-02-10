import winreg
from datetime import datetime
import shutil

UNINSTALL_PATHS = [
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
    (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
]

def get_used_storage():
    storage_info = shutil.disk_usage('C://')
    used_perc = round(storage_info.used / storage_info.total, 4)
    return used_perc


def get_installed_programs():
    programs = []

    for root, path in UNINSTALL_PATHS:
        try:
            with winreg.OpenKey(root, path) as key:
                for i in range(winreg.QueryInfoKey(key)[0]):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, subkey_name) as subkey:
                            name = query_value(subkey, "DisplayName")
                            size = query_value(subkey, "EstimatedSize")  # KB
                            date = query_value(subkey, "InstallDate")

                            if not name:
                                continue
                            if not size:
                                size = 0
                            if not date:
                                continue

                            try:
                                install_date = datetime.strptime(date, "%Y%m%d")
                            except ValueError:
                                continue

                            programs.append({
                                "name": name,
                                "size_mb": round(size / 1024, 1),
                                "install_date": install_date,
                                "age_days": (datetime.now() - install_date).days,
                                "remove_score": (datetime.now() - install_date).days * size//1024
                            })

                    except OSError:
                        continue
        except FileNotFoundError:
            continue

    return programs


def query_value(key, value_name):
    try:
        value, _ = winreg.QueryValueEx(key, value_name)
        return value
    except FileNotFoundError:
        return None


def get_oldest_and_largest(programs, limit=30):
    programs.sort(
        key=lambda p: (p["remove_score"]),
        reverse=True
    )
    return programs[:limit]


def print_candidates(programs):
    print(f"{'Program':40} {'Size (MB)':>10} {'Installed':>12} {'Age (days)':>10}")
    print("-" * 80)
    for p in programs:
        print(f"{p['name'][:38]:40} {p['size_mb']:>10} {p['install_date'].date()} {p['age_days']:>10}")


if __name__ == "__main__":
    used_storage = get_used_storage()
    perform = True
    if used_storage < 0.5:
        print(f"{round(used_storage * 100, 2)}% of your storage space is used, so you don't have to worry about this.")
        print("If you still want to see your storage type 'y' if not type 'n'", end=": ")
        ans = str(input()).lower()
        if ans == 'y':
            perform = True
        elif ans == 'n':
            perform = False
        else:
            raise Exception("Invalid input")
    if perform:
        programs = get_installed_programs()
        programs_sorted = get_oldest_and_largest(programs)
        print_candidates(programs_sorted)