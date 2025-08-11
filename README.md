# Introduction to the Robot Operating System – Simulating with ROS

This project is divided into several parts where you will progressively build a robotic simulation using ROS, develop a reactive navigation node, and perform SLAM mapping. Each step is designed to help you learn the basics of robotics with ROS and simulation in Stage.

---

## Craft 6B (Simulating with ROS) – Part 1: Package Creation and Simulation in Stage

### Objectives:
- Create a ROS package named `simstage_groupX` (where `X` is your group number).
- Inside this package, set up all the necessary files to simulate a virtual world containing a robot in Stage.
- Obtain or create a map for your simulation.  
  > *Tip:* You can search for occupancy grid maps online.  
  > *Note:* The `.pgm` format is just another bitmap image format similar to `.png`.

### Technical details:
- Your robot should be composed of **at least 3 polygonal blocks**.  
- Creativity in your robot’s design will earn you extra points.

### To do:
- Create a folder `simstage_groupX` with a typical ROS package structure (`src`, `launch`, `worlds`, etc.).
- Prepare a `.world` file for Stage that includes your map and robot.
- Define your robot model with its 3 polygonal blocks in a `.yaml` or `.model` file.

---

## Craft 6B (Simulating with ROS) – Part 2: Reactive Navigation

### Objectives:
- Add a ROS node to your package that implements a reactive navigation strategy.
- The robot should be able to:
  - Avoid obstacles without collisions.
  - Move continuously to eventually explore all areas of the environment (no stopping).

### Constraints:
- Unlike the tutorial example, your robot **must never stop moving**.
- Take inspiration from random walk behaviors and/or wall-following robots.

### To do:
- Write a ROS node (in Python or C++) that subscribes to sensor data (e.g., laser scans) and publishes velocity commands (`cmd_vel`).
- Implement the reactive navigation logic inside this node.

---

## Craft 6B (Simulating with ROS) – Part 3: SLAM with Gmapping

### Objectives:
- Install the SLAM package `gmapping`:  
  ```bash
  sudo apt install ros-$ROS_DISTRO-gmapping
