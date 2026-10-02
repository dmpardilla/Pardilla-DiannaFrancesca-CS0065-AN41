# GridDrift: Multi-Agent Random Walk Simulation

**Author:** Dianna Francesca M. Pardilla  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Date:** October 2, 2026  
**Professor:** Ms. Crisola G. Tan  

---

## Overview
This repository contains the complete laboratory implementation and documentation for **Technical Assessment 1: Random Walk Simulation Using AgentPy**. 

The project investigates multi-agent stochastic systems within an enclosed discrete coordinate space. It demonstrates agent initialization, coordinate clamping boundaries, weighted directional movement, real-time path tracing, and final spatial distribution analysis using Python's `agentpy` and `matplotlib` libraries.

---

## Repository Contents

* `TA1_Pardilla.py` — Baseline interactive script implementing uniform random walks and path-tracing animations on a 2D coordinate grid.
* `TA1 Modified_Pardilla.py` — The enhanced script featuring customized title banners, weighted directional drift (40% bias toward moving Right), step-by-step path persistence, and automatic end-of-simulation coordinate summary logging.
* `TA1_Pardilla.pdf` — The primary submission document containing the complete theoretical background, source codes, and answered assessment questions.
* `TA1_Evidence_Pardilla.pdf` — The step-by-step verification and evidence document presenting package installations, terminal commands, experiment runs, and animated plot outputs.

---

## Features & Implementation Details

* **Bounded Coordinate Clamping:** Agents are confined strictly within the dimensions of the grid environment using mathematical min/max clamping logic (`max(0, min(grid_size - 1, coordinate + step))`). This prevents index-out-of-bounds exceptions and keeps agents along border perimeters when boundary collisions occur.
* **Real-Time Trajectory Tracking:** Each walker maintains an internal history log (`self.trajectory`). Starting coordinates and subsequent frame movements are appended step-by-step, allowing `matplotlib` to render historical travel paths across the entire simulation duration.
* **Weighted Directional Drift (Behavioral Modification):** Rather than standard uniform 25% random orthogonal walks, agents utilize a non-uniform probability distribution using `random.choices`:
  * **Right `(1, 0)`:** 40% probability
  * **Left `(-1, 0)`:** 20% probability
  * **Up `(0, 1)`:** 20% probability
  * **Down `(0, -1)`:** 20% probability  
  This introduces an intentional directional bias (eastward drift) across the spatial grid.
* **Dynamic Matplotlib Animation:** Utilizes `matplotlib.animation.FuncAnimation` to clear and redraw coordinate states on each step, displaying current agent coordinates alongside their line trails.
* **Automated Terminal Reporting:** When the simulation concludes, the `end()` method triggers an automated summary in the console that reports each agent's starting position, final resting coordinates, and cumulative path length.