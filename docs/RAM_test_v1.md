# The first version of the RAM test

[RAM test](/src/Benchmark_application/measuring_module/RAM_test.py)

## What does this component do?
This is one of three components in the measuring module of the benchmark application. In the measuring module, data will be collect to see how well the machine can perform video game like test. This module is just to see can this machine run video games well and how much better will it be able to run video games after the perfomance is boosted?

This RAM measuring component measures two things: the avaible ram and the swap memory. The avaible memory is measured to see wether the machine has enough ram avaiable to run basic video games and if the avaible ram is too low it is probably caused by a bottleneck that has to be fixed in another application. The swap memory is measured to see if the machine uses swap memory because this can  greatly impact the speed with which you can play video games.
After this data is measured an objective score is given based on the avrage avaible ram over a certain time period and the avrage swap memory used also over the same time period. 

## How does this fit into the system
This component is an important part of the measuring module in the benchmark application. RAM is very important when running high quality video games so it important to see how much RAM is potentially being used up by the OS or other applications to see wether this system can fix them. It is import to get a clear picture of how much this project can improve the RAM usage of a device.
