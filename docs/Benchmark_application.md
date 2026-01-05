# The first application is finished
**This is the first application that has been finished. This application is mainly used as a benchmark to clearly see the before and after effects of the whole program.**

## What it does
In a nutshell, this program measures the CPU, the RAM, and the storage on a device. It then uses this data to get an idea of how well the device could run a modern-day video game.  
First, it performs a CPU benchmark, meaning it does three different game-specific tests and then runs them to see if the device can perform them within a given time interval. For more information, look at my full documentation of this program [here](/docs/CPU_benchmark_v1.md).

The second component of this application is the RAM benchmark. This simple program first measures the amount of available RAM and then looks for latency by checking for swaps, which could significantly slow down the device and cause lag in video games.

The last program measures some metrics of the storage to see how healthy it is for running video games. It first looks at the percentage of storage being used and then measures the disk read speed.

All the data from these three tests is put together and given different weights to form a weighted average. This weighted average is then used to get a score out of 20 for the overall computer health in regards to playing video games.

## Why I made this application
This is the first application in the whole system. Like I said earlier, I made this to serve as a benchmark that could be used to see the before and after results. Some of the features in this program will later be used in other applications, mostly from the CPU test, because it gathers a lot of data that can be used to look for potential bottlenecks.

## What could be improved
Firstly, I am very happy with this application. It is a huge achievement for me, and I am mostly satisfied with the way it turned out. However, after using this program on other devices, I found that I got higher scores than I expected. On one device, I even got a better score than on my current computer, although this device can run video games a lot worse.

My idea is that this is caused because the RAM score is not based on the right metrics and the weighted average that forms the final score. Firstly, the RAM benchmark measures the percentage of RAM that is still available. This would be a good metric if all devices had the same amount of RAM. However, some of my older devices had a lot less RAM, but because percentage-wise they had more available, they got a higher score. This needs to be fixed in the future by using available RAM not as a percentage, but as a number of bytes.

Secondly, the weighted average is not configured correctly. Currently, 40% of the total score is based on the CPU, 30% on RAM, and 30% on storage. I think the CPU should make up a bigger part of the final score due to its importance, and especially the storage should make up a much smaller part of the total score, because it does not influence the gaming experience as much as the CPU does. I still need to find the correct weights for each of these three criteria.

Even though there is still some work to be done, I am very proud of this achievement and will now be turning my attention to the second application. This second application will look for bottlenecks that might be slowing down the computer.
