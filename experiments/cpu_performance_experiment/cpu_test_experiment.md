# CPU Benchmark Experiment: General Test vs Gaming Test

## Why This Experiment Was Done

The purpose of this experiment was to check if a general CPU benchmark measures the same performance as a gaming-style CPU benchmark.

Many benchmarks claim to show “gaming performance”.
But games do not use the CPU in the same way as simple math tests.

This experiment tries to find out:
- Do both tests measure the same thing?
- Or do gaming workloads stress the CPU differently?

---

## Idea Behind the Experiment

Two different CPU tests were created:
- A general CPU test
- A gaming-oriented CPU test

Both tests were run on different computers.

The execution times were compared.
If both tests measured the same CPU performance, the ratio between them should be similar on all devices.

If the ratios were different, this would mean that gaming workloads behave differently.

---

## The CPU Tests

### General CPU Test

This test focuses on:
- Floating point calculations
- Repetitive math loops
- Predictable code execution

This represents a common synthetic CPU workload.

---

### Gaming CPU Test

This test simulates common game behavior:
- Object movement updates
- Integer calculations
- Branch-heavy logic (prime numbers)
- Matrix and vector math using NumPy

The goal was not to copy a real game, but to imitate typical game-engine patterns.

---

## Test Devices

The tests were run on three different systems:

1. **HP Pavilion**
   - Intel Core i5-1135G7
2. **ThinkPad T450**
   - Older Intel Core i5
3. **Acer Chromebook 11**
   - Intel Celeron N3450

Each test was executed multiple times.
Average execution times were used.

Both single-core and multi-core modes were tested.

---

## How Results Were Compared

For each device:
- The average time of the general CPU test was measured
- The average time of the gaming CPU test was measured

The following ratio was calculated:

Gaming Test Time / General Test Time


This ratio was compared between devices.

---

## Observations

### Single-Core Results

- On modern CPUs, the gaming test was relatively faster.
- On weaker CPUs, both tests performed almost the same.

This suggests that gaming workloads benefit from:
- Better branch prediction
- Faster cache access
- Newer CPU architectures

---

### Multi-Core Results

The multi-core results varied a lot between devices.

This shows that:
- Multi-core performance depends strongly on workload structure
- Running many independent processes does not reflect real game behavior
- Operating system scheduling has a large impact

---

## What Can Be Concluded

This experiment shows that:
- A general CPU benchmark does not represent gaming performance well
- Gaming workloads stress different parts of the CPU
- There is no fixed performance ratio between general and gaming tests
- Single-core performance is often more important for games

---

## Meaning for This Portfolio Project

The goal of this project should not be to “make the CPU faster”.

Instead, useful improvements focus on:
- Better CPU scheduling
- Reducing background tasks
- Improving cache usage
- Optimizing thread priorities

These changes improve real gaming performance, not just benchmark scores.

---

## Limitations of the Experiment

This experiment has limitations:
- The multi-core gaming test does not use shared workloads
- Real games use synchronized threads
- GPU behavior was not simulated
- Power and thermal limits were not controlled

---

## Possible Improvements

Future versions of this experiment could:
- Simulate a main game thread with worker threads
- Limit the number of active CPU cores
- Measure frame-time consistency instead of total runtime
- Reduce Python interpreter overhead

---

## Final Summary

Gaming performance cannot be accurately measured with simple CPU benchmarks.

Understanding how workloads behave is more important than raw numbers.

This experiment helps guide the next steps of this portfolio project.
