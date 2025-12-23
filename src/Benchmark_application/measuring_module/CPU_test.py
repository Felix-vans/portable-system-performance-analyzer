import time
from time import perf_counter
import random
import numpy as np
import heapq


# Global test data (created once, reused every frame)

POINT_COUNT = 200
points = []
velocities = []

for _ in range(POINT_COUNT):
    points.append([random.random(), random.random(), random.random()])
    velocities.append([random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)])

MATRIX_POINT_COUNT = 100_000
matrix_points = np.random.rand(MATRIX_POINT_COUNT, 3).astype(np.float64)

rotation_matrix = np.array([
    [0.99, -0.05, 0.0],
    [0.05,  0.99, 0.0],
    [0.08,  0.0,  1.0]
])


# Test 1: Object movement (game logic / integer math)

def object_movement_test(iterations: int):
    """Simulates simple game logic: object position updates."""
    dt = 1 / 60

    start = perf_counter()
    for _ in range(iterations):
        for i in range(POINT_COUNT):
            for axis in range(3):
                points[i][axis] += dt * velocities[i][axis]
    return perf_counter() - start



# Test 2: Prime calculation (branch-heavy integer logic)

def prime_calculation_test(iterations: int):
    """Simulates branch-heavy CPU logic similar to AI decisions."""
    start = perf_counter()
    for _ in range(iterations):
        primes = [2]
        n = 3
        while len(primes) < 500:
            is_prime = True
            for p in primes:
                if n % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
            n += 1
    return perf_counter() - start



# Test 3: Matrix transforms (SIMD / FP heavy)

def matrix_transform_test(iterations: int):
    """Simulates transform-heavy workloads (animations, physics)."""
    pts = matrix_points

    start = perf_counter()
    for _ in range(iterations):
        pts = pts @ rotation_matrix.T
    return perf_counter() - start



# Frame simulation test

def frame_test(
    movement_iters: int,
    prime_iters: int,
    transform_iters: int,
    duration_seconds: int,
    target_fps: int
):
    """Runs a fixed-time frame simulation and records frame times."""
    frame_times = []
    test_start = perf_counter()

    while perf_counter() - test_start < duration_seconds:
        frame_start = perf_counter()

        object_movement_test(movement_iters)
        prime_calculation_test(prime_iters)
        matrix_transform_test(transform_iters)

        frame_times.append(perf_counter() - frame_start)

    frame_budget = 1 / target_fps
    dropped_frames = sum(1 for t in frame_times if t > frame_budget)

    return dropped_frames, len(frame_times), frame_times



# Benchmark configuration

MOVEMENT_ITERS = 50
PRIME_ITERS = 1
TRANSFORM_ITERS = 9
TARGET_FPS = 60
TEST_DURATION = 5  # seconds
scores = []

# Run test 10 times
for _ in range(10):
    dropped, total_frames, frame_times = frame_test(
        MOVEMENT_ITERS,
        PRIME_ITERS,
        TRANSFORM_ITERS,
        TEST_DURATION,
        TARGET_FPS
    )

    drop_percentage = (dropped / total_frames) * 100


    # Frame-time analysis

    average_frame_ms = (sum(frame_times) / total_frames) * 1000

    worst_10_frames = heapq.nlargest(10, frame_times)
    worst_10_avg_ms = (sum(worst_10_frames) / 10) * 1000
    worst_frame_ms = max(worst_10_frames) * 1000

    spike_threshold = 1.2 * (1 / TARGET_FPS)
    spike_count = sum(1 for t in frame_times if t > spike_threshold)


    # Scoring

    FRAME_BUDGET_MS = 16.7

    smooth_penalty = max(0, (average_frame_ms - FRAME_BUDGET_MS) / FRAME_BUDGET_MS) * 10

    stutter_score = (
        (drop_percentage / 50) * 5 +
        (worst_10_avg_ms / (FRAME_BUDGET_MS * 1.5)) * 3 +
        (spike_count / 50) * 2
    )

    stability_penalty = min(10, stutter_score)

    score = 20 - (smooth_penalty + stability_penalty)
    score = round(min(20, max(0, score)), 2)
    scores.append(score)

final_score = (scores[4] + scores[5]) / 2 # Median score

# Output

print(f"Average frame time: {round(average_frame_ms, 3)} ms")
print(f"Dropped frames: {round(drop_percentage, 2)}%")
print(f"Spike frames (>120%): {spike_count}")
print(f"Worst frame time: {round(worst_frame_ms, 3)} ms")
print(f"Average of worst 10 frames: {round(worst_10_avg_ms, 3)} ms")

print(f"\nYour device scored {final_score}/20 (median)")
