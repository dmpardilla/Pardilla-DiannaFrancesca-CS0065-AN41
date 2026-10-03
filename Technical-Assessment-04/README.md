# Technical Assessment 4: Workstation & Server Diagnostic Reasoning Suite

**Authors:** Dianna Francesca M. Pardilla & Justin D. Vergara  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Date:** October 3, 2026  
**Professor:** Ms. Crisola G. Tan  

---

## Overview
This repository contains the laboratory implementation and technical documentation for **Technical Assessment 4: Implementing Knowledge Representation, Rule-Based Reasoning (RBR), and Case-Based Reasoning (CBR)**. 

The project implements an automated **Workstation and Server Diagnostic System** that monitors real-time telemetry, protects hardware through deterministic rule evaluation, and resolves multi-symptom faults through experience-based case retrieval and retention. The suite contrasts the rigid, fast execution of **Rule-Based Reasoning** with the adaptive, memory-driven **Case-Based Reasoning 4R Cycle (Retrieve, Reuse, Revise, Retain)**.

---

## Repository Contents

* `TA4_Pardilla_Vergara.py` — Complete executable Python script featuring knowledge representation structures, rule-based inference logic, similarity-based case retrieval, dynamic retention, and an interactive button-styled ANSI terminal menu.
* `TA4_Pardilla_Vergara_3.pdf` — Formal laboratory submission document containing full source code listings, system use-case descriptions, visual execution traces, and comparative reflections.

---

## Features & Implementation Details

* **Knowledge Representation (KR Working Memory):**  
  * **Telemetry Schema:** Stores 7 hardware and environmental facts across 3 distinct operational categories.
  * **Thermals & Environment:** Monitors `core_temperature_celsius` (86°C) and `ambient_humidity_percent` (74%).
  * **Resource Utilization & Power:** Tracks `cpu_load_percent` (96%), `cooling_pump_active` (False), and `battery_charge_percent` (15%).
  * **System Health & Hardware Flags:** Detects `disk_io_errors` (True) and measures `network_latency_ms` (350 ms).

* **Rule-Based Reasoning Engine (RBR Production System):**  
  * **Deterministic Rules:** Evaluates live working memory against defined conditional policies to trigger immediate safety interventions.
  * **`RBR-01` (Thermal Critical):** If core temperature exceeds 80°C, the system triggers immediate CPU clock down-throttling.
  * **`RBR-02` (Cooling Failure):** If core temperature exceeds 75°C and cooling pump is offline, the system bypasses auxiliary high-RPM fan controls.
  * **`RBR-03` (Battery Preservation):** If battery charge drops below 20%, secondary GPU threads and background tasks are terminated.
  * **`RBR-04` (Disk Anomaly):** If disk I/O error flags are asserted, the primary file-system partition is mounted as read-only.

* **Case-Based Reasoning Engine (CBR 4R Cycle):**  
  * **Case Base Representation:** Archives historical troubleshooting cases mapping boolean symptom vectors (`overheating`, `fan_spinning`, `loud_buzzing`, `blue_screen`) to verified technical solutions.
  * **Retrieve:** Calculates feature overlap percentage to rank historical cases and identify the highest-scoring analog.
  * **Reuse:** Extracts the verified solution from the top-matching historical case.
  * **Revise:** Facilitates human-in-the-loop adaptation, allowing the user to provide customized fixes or automatically append addendums.
  * **Retain:** Generates a new unique identifier (e.g., `CASE-105`, `CASE-106`) and saves the newly resolved problem-solution pair directly into active memory without requiring code modification.

* **Terminal UI Engine:**  
  * Utilizes pixel-aligned ASCII borders, color-coded ANSI status tags, and tactile button chips (`< >`) for uniform cross-terminal presentation.

---

## Interactive CLI Menu

The program provides an interactive terminal dashboard supporting live diagnosis and inspection:
1. **[1] View Knowledge Base (Part 1 - KR):** Displays the current working memory facts, system metrics, and telemetry states.
2. **[2] Run Rule-Based Reasoning Engine (Part 2 - RBR):** Evaluates all production rules against working memory and prints inferred emergency actions.
3. **[3] Execute Case-Based Reasoning Pipeline (Part 3 - CBR 4R):** Takes an incoming multi-symptom problem vector and executes the full Retrieve, Reuse, Revise, and Retain lifecycle.
4. **[4] View All Retained Cases in Memory:** Displays the entire case repository, including default historical cases and dynamically learned cases.
5. **[5] Exit System:** Closes the diagnostic environment session.

---

## How to Run

1. Clone or download the repository to your local computer.
2. Open a terminal or VS Code in the project directory.
3. Run the script using Python:
   ```bash
   python TA4_Pardilla_Vergara.py