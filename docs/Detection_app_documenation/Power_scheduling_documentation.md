# The first version of the power sheduling module

**This module collects power plan data so it can be used in the third application for advising the user which settings to change.**

## [Power Sheduling](/src/Detection_application/power_scheduling.py)

## What this module does

This program collects data about the power plan settings in windows 11. It looks for 4 specific settings, namely: 
1. The active powerplan
2. The minimum processor state
3. Core parking being turned on
4. Processor boost mode
   
The data is collected using the windows command prompt and registry. The program doesn't change any of the settings. It just collects data about them and tells the user which ones they are **now** using. This information can be used to see which settings might act as a bottleneck for their computers performance.

## How does it fit into the system

This module is part of the second application. This application collects data about certain settings, processes and more to find potential bottlenecks that might be slowing the computer down. pIn the third application (which I haven't started on yet), this data will shown to the user and then the user will be advised on which settings they need to change, processes they need to turn of and more so they have a clear picture of how to improve their computers perfomance.

## How it could be improved

The program isn't perfect yet, but it is now at a point that I believe I can continue to the next modules and leave this as is and improve it in the future.


Thing I will improve in the future are firstly making a function for slicing and splitting the output string which I do in almost every part of this module.
Secondly, I might add a  couple more functions for other settings. However, I will have to do more research on which settings of the power plan might slow the computer down. Lastly, I feel like some parts of the code are unnecessarly complicated or long and I feel like I can simplify them and make the more efficient. I will need to further improve my coding skills to find and improve these messy parts of my code.
