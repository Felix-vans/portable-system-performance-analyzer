import os
import pandas as pd
import csv


TASKLIST_PATH = "C:/PREF_USB/experiments/tasks.csv"

def all_processes():
    os.system(f'cmd /c "tasklist /FO csv > {TASKLIST_PATH}"')

    processes = {
        'name': [],
        'mem': [],
        'count': []
    }


    with open(TASKLIST_PATH, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # skip header

        for row in reader:
            try:
                name = row[0]
                memory_kb = float(row[4].replace(" K", "").replace(".", ""))
                processes['name'].append(name)
                processes['mem'].append(memory_kb)
                processes['count'].append(1)

            except (IndexError, ValueError):
                continue
    
    return processes

def nlargest(n: int, list):
    dataframe = pd.DataFrame(list)

    dataframe = dataframe.groupby('name', as_index=False).sum()

    top_n = dataframe.nlargest(n, 'mem')

    return top_n

def main(list):
    for _, row in list.iterrows():
        print(
            f"{row['name']}: "
            f"{row['mem'] / 1024:,.2f} MB "
            f"({int(row['count'])} processen)"
        )

if __name__ == "__main__":
    processes = all_processes()
    top_30 = nlargest(30, processes)
    main(top_30)
