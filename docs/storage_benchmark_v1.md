# The first version of the storage benchmark
---

## [Storage_test](/src/Benchmark%20application/Storage_test.py)

## What does it do?
This program gives a computer a score out of twenty based on two metrics.  
The first metric is the amount of used storage. This is measured because it has been shown that storage performance degrades as it becomes more filled.  
The second metric is disk read speed. This is important because, when playing video games, a large amount of data is continuously read from storage. If the disk read speed is too slow, this can lead to long loading times and in-game delays.

Disk read speed has a larger impact on the final score than used storage. Disk read speeds between 2000 and 5000 MB/s are considered ideal, while anything below this range will result in a below-average score.

## How does this fit into the whole system?
I recently decided not to split the benchmark application into two separate modules, but instead keep it as a single module. The reason for this is that a second module would be too insignificant and would unnecessarily complicate the system.

This program is primarily used to give the computer a score out of twenty that reflects the health of the storage. This score is then passed to another program that also collects scores from the CPU and RAM. That program calculates a weighted average and produces an overall computer health score.

This overall score will be used as a benchmark before and after bottlenecks are identified and resolved, making it possible to clearly measure how much the system’s gaming performance has improved.
