# The first version of the startup app detection and classification component

## [Startup app classifier]("/src/Detection_application/Startupapps.py")

## What it does

This is a component of the Detection application, which is an application that looks for potential performance bottlenecks. I am not yet fully sure about the complete architecture of the Detection Application, but I will put more thought into this later.

This component collects the names of all startup applications and their executable paths. After this data is collected, the applications are classified based on their importance. This part of the program is still very primitive and will require significant improvement over time. For now, I have implemented a basic first-generation classification function.

The classification is mainly based on where the executable is located, such as whether it is in Program Files, AppData, or another location. Based on this, each startup application is assigned an importance level. An application can be rated as **essential**, meaning it should not be disabled; **important**, meaning it can be disabled but doing so is not recommended without further consideration; or **unimportant**, meaning it is generally recommended to disable the startup application if the user does not actively need it.

## How it fits into the whole system

This component is part of the Detection application and will be one of several components that search for different types of bottlenecks. Each component will focus on a specific area of the system and contribute to a broader analysis by identifying and ranking issues based on their potential impact on system performance. The startup application classifier provides early insight into background load at system boot, which can later be combined with other detection results to form a more complete performance overview.
