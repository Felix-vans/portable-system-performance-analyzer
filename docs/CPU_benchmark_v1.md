# The first version of the CPU benchmark
[CPU test](/src/Benchmark%20application/Measuring%20module/CPU_test.py)
---

## How does it work
After the [CPU experiment](/experiments/cpu_test_experiment.md), I concluded a game spcific CPU benchmark would be more suitable for this project. The benchmarks consists of 3 little test that are specifically made to emulate game like calculations. 

### Object movement test

The first test is an object movement test. I began by defining 200 points wiht a random position (x,y,z) and then I gave everypoint a certain speed in the x-, y- and z-axis. These values will stay constant during the entire test. \n\nDuring the test the position of the points will be updated every for a time change of 16.7 ms. The points will be updated for a fixed amount of iterations.

### Prime calculation
The second test is a more integer and branch heavy test which simulates game logic and AI decision making. The test is simple, calculate the first 500 primes. During this test alot of if-else stamentets, loops and arrays are used to simulate game logic.

### Matrix transformations
The third test uses matrix transformations to emulate object movement and orientation, projection, camera control, etc. in video games. First, 100,000 matrices are randomly made and stored in an array. Then, they are transformed using a constant transformation matrix for a fixed amount of iterations

### Giving the computer a score
After these 3 test have been completed the time will stored as one frame. After ten seconds of repeating the tests and storing the frame times, we will give the computer a score out of 20 based on the following benchmarks: the avrage frame time; the percent of frames longer then 16.7 ms; the avrage of the ten slowest frames and the amount of frame times 120% longer than the goal of 16.7 ms. 

This whole process will be repeated ten times and the scores will be saved. After this is finsished, the median of all the scores will be calculated to get a clear objective idea of the computer performance with modern games.

---

## How this will be used in the system
This is the first of 3 benchmarks that will make up the testing module. The testing module will collect the data about the computer. The first benchmark is the CPU test, this one. The second one is a RAM benchmark and storage benchmark.

After all the data is collected for these 3 benchmarks, a different module will analyse the data to give the user a clear picture of how well their device can run video games.

These 2 modules (collecting data and analysing data) will make up the testing application. This application will be used before and after the bottlenecks have been detected and resolved to get a clear picture of how much this project improves a devices performance.