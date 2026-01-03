import time
import shutil

PATH = "C://"
FILE_PATH = "C:/PREF_USB/experiments/big_file.txt"
BLOCK_SIZE = 1024 ** 2  # 1 MB
REPEAT = 10


def storage_filled(path):
    # Get total and used storage in GB
    usage = shutil.disk_usage(path)
    total_gb = usage.total / 10 ** 9
    used_gb = usage.used / 10 ** 9

    used_percent = round((used_gb / total_gb) * 100, 2)
    return used_percent


def disk_read_speed():
    total_bytes = 0
    start_timer = time.perf_counter()

    with open(FILE_PATH, 'rb') as file:
        while True:
            data = file.read(BLOCK_SIZE)
            if not data:
                break
            total_bytes += len(data)

    duration = time.perf_counter() - start_timer
    speed_mb_s = (total_bytes / (1024 * 1024)) / duration

    return speed_mb_s


def score():
    # Storage usage penalty
    storage_used = storage_filled(PATH)
    storage_penalty = min(max(storage_used - 50, 0) / 2, 20)

    # Disk speed score
    disk_speed = disk_read_speed()
    if disk_speed < 500:
        disk_speed_score = disk_speed / 62.5
    elif disk_speed < 2000:
        disk_speed_score = ((disk_speed - 500) / 214.28) + 8
    elif disk_speed < 5000:
        disk_speed_score = ((disk_speed - 2000) / 750) + 15
    else:
        disk_speed_score = min(((disk_speed - 5000) / 2000) + 19, 20)

    final_score = round(disk_speed_score - (storage_penalty * 0.3), 2)
    return final_score


def main():
    scores = []

    for _ in range(REPEAT):
        scores.append(score())

    avg_score = round(sum(scores) / REPEAT, 2)
    print(f"This is how your storage scored: {avg_score}/20.")

if __name__ == "__main__":
    main()
