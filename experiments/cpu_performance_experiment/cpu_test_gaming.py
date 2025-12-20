import time
from time import perf_counter
import random
import numpy as np
import multiprocessing as mp


# -----------------------------
# Test 1: Object movement (game logic / integer math)
# -----------------------------
def object_moving_test(iterations=20000):
    points = []
    velocity = []

    for _ in range(500):
        points.append([random.random(), random.random(), random.random()])
        velocity.append([random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)])

    dt = 1 / 60

    start = perf_counter()
    for _ in range(iterations):
        for i in range(500):
            for j in range(3):
                points[i][j] += dt * velocity[i][j]
    end = perf_counter()

    total_time = end - start

    return total_time


# -----------------------------
# Test 2: Prime calculation (branching / integer heavy)
# -----------------------------
def primes_calc(iterations=10):
    start = perf_counter()
    for _ in range(iterations):
        primes = [2]
        n = 3
        while len(primes) < 5000:
            is_prime = True
            for p in primes:
                if n % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
            n += 1
    end = perf_counter()

    total_time = end - start
    
    return total_time

# -----------------------------
# Test 3: Matrix transforms (SIMD / FP heavy)
# -----------------------------
def transforms_test(iterations=600):
    n_points = 1_000_000
    pts = np.random.rand(n_points, 3).astype(np.float64)

    R = np.array([[0.99, -0.05, 0.0],
                  [0.05,  0.99, 0.0],
                  [0.08,  0.0,  1.0]])

    start = perf_counter()
    for _ in range(iterations):
        pts = pts @ R.T
    end = perf_counter()

    total_time = end - start
    
    return total_time

def worker():
    object_moving_test()
    primes_calc()
    transforms_test()


def run_multicore():
    num_cores = mp.cpu_count()
    processes = []

    start = perf_counter()

    for _ in range(num_cores):
        p = mp.Process(target=worker)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = perf_counter()

    print(f"Multicore test ({num_cores} cores): {end - start:.4f} sec")



# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    print("Starting single core CPU gaming-style benchmark...\n")

    test_1 = object_moving_test()
    print(f"[Object movement] {20000} iteraties in {test_1:.4f} sec")
    print(f"Gemiddeld: {20000/test_1:.6f} iteratie per seconde\n")
    test_2 = primes_calc()
    print(f"[Prime calc] {10} runs in {test_2:.4f} sec")
    print(f"Gemiddeld: {test_2 / 10:.6f} sec per run\n")
    test_3 = transforms_test()
    print(f"[Transforms] {600} iteraties in {test_3:.4f} sec")
    print(f"Gemiddeld: {600/test_3:.6f} iteratie per seconde\n")

    print("Benchmark finished.")

    all_total_time_single_core = test_1 + test_2 + test_3
    print(f'Total time single core tests: {all_total_time_single_core}')

    print("Starting multicore CPU gaming-style benchmark...\n")
    run_multicore()


    

