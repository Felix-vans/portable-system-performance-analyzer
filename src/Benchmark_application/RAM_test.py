import psutil
import time

TIME_TEST = 5  # duration of each measurement in seconds


def available_ram():
    ram_percentages = []
    start_timer = time.perf_counter()

    while time.perf_counter() - start_timer < TIME_TEST:
        free_ram_percent = 100 - psutil.virtual_memory().percent
        ram_percentages.append(free_ram_percent)
        time.sleep(0.25)

    avg_available_ram = sum(ram_percentages) / len(ram_percentages)
    return avg_available_ram


def swap_used():
    swap_percentages = []
    start_timer = time.perf_counter()

    while time.perf_counter() - start_timer < TIME_TEST:
        swap_percent = psutil.swap_memory().percent
        swap_percentages.append(swap_percent)
        time.sleep(0.25)

    avg_swap_used = sum(swap_percentages) / len(swap_percentages)
    return avg_swap_used


def score():
    ram = available_ram()
    swap = swap_used()

    # RAM score (0–14)
    if ram >= 70:
        ram_score = 14
    elif ram >= 50:
        ram_score = 11
    elif ram >= 30:
        ram_score = 8
    elif ram >= 15:
        ram_score = 4
    else:
        ram_score = 1

    # Swap penalty (0–6)
    if swap <= 1:
        swap_penalty = 0
    elif swap <= 5:
        swap_penalty = 2
    elif swap <= 15:
        swap_penalty = 4
    else:
        swap_penalty = 6

    total_score = ram_score + (6 - swap_penalty)

    return total_score


def main():
    ram = available_ram()
    swap = swap_used()
    print(f'Average available RAM: {ram:.1f}%')
    print(f'Average swap usage: {swap:.1f}%')
    print(f'RAM performance score: {score()}/20')

if __name__ == "__main__":
    main()
