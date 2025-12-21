import time
from time import perf_counter
import random
import numpy as np
import multiprocessing as mp

def single_core_test(iterations, repetitions):
    total_duration = 0
    print("Starting single core test...")
    for attempt in range(repetitions):
        start = perf_counter()
        for _ in range(iterations):
            for x in range(1, 1000):
                3.141592 * 2 ** x # Multiplying the number Pi by 2 to the power of x
            for x in range(1, 10000):
                float(x) / 3.141592 # Dividing x by Pi
            for x in range(1, 10000):
                float(3.141592) / x # Dividing the number Pi by x 
        end = perf_counter()
        duration = end - start
        total_duration += duration
        print(f'Attempt {attempt + 1}: {duration}s')
    return total_duration

def multicore_worker(args):
    iterations, repetitions = args
    total_ops = 0
    start = perf_counter()

    for _ in range(repetitions):
        for x in range(1, 1000):
            3.141592 * 2 ** x
        for x in range(1, 10000):
            float(x) / 3.141592
        for x in range(1, 10000):
            float(3.141592) / x
        total_ops += 1

    end = perf_counter()
    return end - start, total_ops

if __name__ == '__main__':
    try:
        print('Single core CPU test is starting...')

        # Benchmark parameters
        iterations = 10000
        repetitions = 10

        # Run Single-core CPU test
        total_time = single_core_test(iterations, repetitions)
        avg_time_rep = total_time / repetitions
        iterations_per_sec = iterations / avg_time_rep
        print(f'The total time for the test: {total_time}.\nThe avrage time per rep: {avg_time_rep}\nThe amount of iterations per second: {iterations_per_sec}.')


        # Run multicore test
        print('\nMulticore test is starting...\n')
        num_cores = mp.cpu_count()
        print(f'Utilizing {num_cores} cores for the test...\n')

        chunk_size = iterations // int(num_cores)
        args = [(iterations, chunk_size)] * num_cores

        total_ops = 0
        start = perf_counter()
        
        with mp.Pool(processes=num_cores) as pool:
            results = []
            for idx, (avg, ops) in enumerate(pool.imap_unordered(multicore_worker, args), start=1):
                print(f'Core {idx} finished: {avg}s')
                results.append(avg)
                total_ops += ops

        end = perf_counter()
        total_time = end - start

        print(f'\nMulticore Results:')
        print(f'Total wall time: {total_time}s')
        print(f'Total operations completed: {total_ops}')
        multi_ops_per_second = total_ops / total_time
        print(f'Multi-Core Operations per second: {int(multi_ops_per_second)}')
    
    except KeyboardInterrupt:
        print("\nBenchmark interrupted. Exiting...")
        exit(1)

