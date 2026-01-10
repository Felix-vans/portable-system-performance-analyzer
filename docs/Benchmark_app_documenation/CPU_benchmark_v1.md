# The First Version of the CPU Benchmark  
[CPU test](/src/Benchmark%20application/Measuring%20module/CPU_test.py)

---

## How Does It Work
After the [CPU experiment](/experiments/cpu_test_experiment.md), I concluded that a game-specific CPU benchmark would be more suitable for this project. The benchmark consists of three small tests that are specifically made to emulate game-like calculations.

### Object Movement Test

The first test is an object movement test. I began by defining 200 points with a random position (x, y, z), and then I gave every point a certain speed in the x-, y-, and z-axis. These values stay constant during the entire test.

During the test, the position of the points is updated every time with a time change of 16.7 ms. The points are updated for a fixed amount of iterations.

### Prime Calculation

The second test is a more integer- and branch-heavy test, which simulates game logic and AI decision-making. The test is simple: calculate the first 500 prime numbers. During this test, a lot of if-else statements, loops, and arrays are used to simulate game logic.

### Matrix Transformations

The third test uses matrix transformations to emulate object movement and orientation, projection, camera control, etc. in video games. First, 100,000 matrices are randomly generated and stored in an array. Then, they are transformed using a constant transformation matrix for a fixed amount of iterations.

### Giving the Computer a Score

After these three tests have been completed, the time is stored as one frame. After ten seconds of repeating the tests and storing the frame times, the computer is given a score out of 20 based on the following benchmarks: the average frame time; the percentage of frames longer than 16.7 ms; the average of the ten slowest frames; and the amount of frame times that are 120% longer than the goal of 16.7 ms.

This whole process is repeated ten times, and the scores are saved. After this is finished, the median of all the scores is calculated to get a clear and objective idea of the computer’s performance with modern games.

---

## How This Will Be Used in the System

This is the first of three benchmarks that will make up the testing module. The testing module collects data about the computer. The first benchmark is the CPU test, this one. The second one is a RAM benchmark, and the third one is a storage benchmark.

After all the data is collected for these three benchmarks, a different module analyses the data to give the user a clear picture of how well their device can run video games.

These two modules (collecting data and analysing data) make up the testing application. This application is used before and after bottlenecks have been detected and resolved to get a clear picture of how much this project improves a device’s performance.

