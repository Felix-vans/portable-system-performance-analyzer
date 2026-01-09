# First Version of the RAM Usage Analyzer

## [RAM Usage Analyzer](/src/Detection_application/RAM_usage.py)

## How It Works
The program retrieves RAM usage data from the Task Manager and loads it into a DataFrame using pandas. One issue I noticed is that many applications are split into multiple processes. This makes it harder to get a clear overview of which applications are using the most RAM.

To solve this, all processes with the same name are grouped together and their RAM usage is summed. This provides a clearer picture of overall RAM usage per application.

## How This Program Fits into the System
This program is part of the detection application. Its main goal is to identify which processes are using the most RAM. In a later stage, I will develop a module that analyzes this data and provides the user with guidance on which processes can be safely disabled and which ones should remain active.

## Planned Improvements
This program is not finished yet. In the future, RAM usage will be measured multiple times over a fixed time interval. The average of these measurements will then be calculated to reduce the impact of short-lived usage spikes.

In addition to the average, the maximum RAM usage will also be recorded to give insight into how high these spikes can be.
