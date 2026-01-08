import psutil
import pandas as pd

def get_running_processes():
    process_list = []

    for process in psutil.process_iter(['pid', 'name', 'username', 'memory_info', 'cpu_percent', 'status', 'create_time']):
        try:
            process_list.append({
                'PID': process.info['pid'],
                'Process Name': process.info['name'],
                'User': process.info['username'],
                'Memory (MB)': process.info['memory_info'].rss / (1024 * 1024),  # Convert to MB
                'CPU (%)': process.info['cpu_percent'],
                'Status': process.info['status'],
                'Start Time': pd.to_datetime(process.info['create_time'], unit='s')
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Skip inaccessible processes

    return pd.DataFrame(process_list)

# Fetch process details
df = get_running_processes()

# Print the DataFrame (for debugging)
print(df)
