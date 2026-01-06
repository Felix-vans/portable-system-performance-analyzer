import subprocess

def split(string: str):
        last = 0
        list = []
        for i in range(len(string)):
            if ord(string[i]) == 10:
                list.append(string[last:i])
                last = i + 1
        return list


def collect_data():

    name_output = subprocess.check_output(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_StartupCommand | Select-Object -ExpandProperty Name"
        ],
        text=True
    )

    path_output = subprocess.check_output(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_StartupCommand | Select-Object -ExpandProperty Command"
        
        ],
        text=True
    )

    names = split(name_output)
    paths = split(path_output)
    startup_apps =[names, paths]

    return startup_apps

def classify(startup_apps):
    # classify based on what it is and how necassry it is to the system as a startup application
    essential = []
    important = []
    unimportant = []
    for i in range(len(startup_apps[1])):
        if startup_apps[1][i].find("C:\\") == -1:
             essential.append(startup_apps[0][i])
        
        elif startup_apps[1][i].find("Program Files") != -1 or startup_apps[1][i].find("Program Files (x86)") != -1:
             important.append(startup_apps[0][i])
             
             
        elif startup_apps[1][i].find("AppData") != -1:
             unimportant.append(startup_apps[0][i])
             
         
    return [essential, important, unimportant]

def main():
    data = collect_data()
    report = classify(data)

    print("These startupapps are essential so DO NOT turn them off: ", end=" ")
    for i in report[0]:
         print(i, end=", ")
    print("\n\n")
    print("These startupapps might be important, if these seem unimportant to you, you can turn them off but be causeous and do research: ", end="")
    for i in report[1]:
         print(i, end=", ")
    print("\n\n")
    print("These startup apps are most likely unimportant, if you don't use them often it is recommended to turn them off: ", end="")
    for i in report[2]:
         print(i, end=", ")
         

if __name__ == "__main__":
    main()



