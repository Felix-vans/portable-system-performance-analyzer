# The Performance Benchmarkt application of this project

**The first application I will me making in this project is a performance benchmarkt. This benchmark will be performed before and after the bottleneck detection and solution applications. Thus we can get a clear picture of how much the system actually improves game specific performance. This application will consist of two modules, one that performs the benchmarks and another that interperts the data and gives the device a clear performance score.**

---

## The first module - measuring the performance
The module will consist of three modules that measure the overall system performance.

First, this component will include a game specific CPU test. I already have a simple gaming-specific CPU benchmark used in my [CPU performance experiment](/experiment/cpu_performance_experiment/cpu_test_experiment.md). I will be improving upon this programm by adding more suphisticated test that are even more catered towards gaming-specific performance. This will include: [to be filled in].

Second, I will add a component that measures the RAM performance. It will be measuring for errors, speed and latency. 

The third and last componenet I will add is going to measure the overall storage health and stability. These tests will measure for troughput (MB/s), Input/Output Operations per Second and latency.

---

## The second module - analysing the perfomance
Once all the data has been collected another module will interpret the data. It will give the device a score on 20 based on the time it got compared to avrage time for that type of CPU. This is how the score will be measured:
```
score = (measured_value / expected_average) * 10
```
Meaning, if the measured value is 2 or more times better then the avrage it will get perfect score 20/20.
Then we will implement a weighted avrage for all the components of the benchmark so we get a clear objective picture of the overall health of the device and how much will have to be improved upon:
```
Total Score (0–20) =
CPU_score * 0.5 +
RAM_score * 0.30 +
Storage_score * 0.20 
```


