# CleanSweep: 2-Chamber Reflex & 3-Chamber Stochastic Vacuum Simulation

**Author:** Dianna Francesca M. Pardilla  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Date:** October 3, 2026  
**Professor:** Ms. Crisola G. Tan  

---

## Overview
This repository contains the laboratory implementation and technical documentation for **Technical Assessment 2: Rule-Based Agent Simulation**. 

The project models an autonomous vacuum cleaner reflex agent navigating a discrete environment. It covers sensory percept evaluation, condition-action production rules, interactive CLI telemetry cards, and an expanded 3-chamber dynamic matrix model.

---

## Repository Contents

* `TA2_Pardilla.py` — Complete executable Python script containing the 2-chamber production model, 3-chamber stochastic engine, and terminal CLI.
* `TA2_Pardilla, Dianna Francesca M..pdf` — Formal laboratory submission document containing the technical background, full code implementation, and answered assessment questions.
* `TA2_Evidence_Pardilla.pdf` — Evidence compilation document with implementation snapshots, interactive terminal setups, and execution traces.

---

## Features & Implementation Details

* **Environment State Representation (`DualChamberEnvironment`):** Tracks room states using a Python dictionary mapping chamber letters (`'A'`, `'B'`) to `RoomStatus` enums (`DIRTY`, `CLEAN`). Provides sensory verification via `is_dirty()` and state mutation via `clean_room()`.
* **Rule-Based Reflex Architecture (`ReflexVacuumAgent`):** Operates on standard condition-action production rules without maintaining internal state history:
  * **Rule 1 (`[CLEAN]`):** If the current chamber is `Dirty`, sanitize the room and stay put for the cycle.
  * **Rule 2 (`[RELOCATE]`):** If the current chamber is `Clean`, move to the opposite chamber (`A` -> `B` or `B` -> `A`).
* **Real-Time ASCII Telemetry HUD:** Custom ANSI-styled cards display cycle counts, triggered production rules, agent positions, and live chamber statuses across each step.
* **3-Chamber Stochastic Matrix (`MultiChamberEnvironment` & `StochasticMatrixAgent`):** Scales the layout to Chambers A, B, and C. When the current room is clean, the agent identifies polluted nodes using `dirty_nodes()` and navigates toward them, featuring a live ASCII grid display.

---

## How to Run

1. Clone or download the repository to your machine.
2. Ensure VSCODE is installed.
3. Run the script:
   ```bash
   python TA2_Pardilla.py