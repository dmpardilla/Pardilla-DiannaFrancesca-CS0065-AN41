# Case Study 3: Intelligent Tutoring System (ITS) — Case-Based Reasoning Engine

**Authors:** Dianna Francesca M. Pardilla & Justin D. Vergara  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Date:** October 3, 2026  
**Professor:** Ms. Crisola G. Tan  

---

## Overview
This repository contains the laboratory implementation and technical documentation for **Technical Assessment 3: Case-Based Reasoning (CBR) System Development**. 

The project implements an **Intelligent Tutoring System (ITS)** that diagnoses student learning struggles and provides personalized pedagogical guidance following the 4R CBR cycle: **Retrieve, Reuse, Revise, and Retain**. Instead of executing static rules, the system matches new student errors to historical cases, adapts instructional feedback to the learner's profile, and continuously retains new experiences in memory.

---

## Repository Contents

* `its_cbr_system.py` — Complete executable Python script featuring typed dataclass models, weighted similarity matching, rule-based adaptation logic, dynamic retention, and an interactive ANSI terminal menu.
* `TA3_Pardilla_Vergara.pdf` — Formal laboratory submission document containing full source code listings, system documentation, execution traces, and partner reflections.

---

## Features & Implementation Details

* **Case Representation (`ProblemState` & `RemedialIntervention`):**  
  * **Problem Schema:** Tracks learner domain attributes including `topic` (Algebra, Geometry, Calculus), specific flaw `error_type` (Formula Misuse, Sign Error, Unit Mismatch), baseline `proficiency_level` (Beginner, Intermediate, Advanced), and mistake count `error_frequency`.
  * **Solution Schema:** Delivers targeted `intervention` instructions, assigned `recommended_practice` sets, and curriculum pacing under `difficulty_adjustment`.

* **Weighted Similarity Assessment (`calculate_similarity`):**  
  Evaluates problem similarity across categorical matches and normalized numerical differences:
  * **Error Type (40% weight):** Primary focal point ensuring remediation directly aligns with the detected conceptual flaw.
  * **Topic (30% weight):** Ensures domain-specific relevance.
  * **Proficiency Level (15% weight):** Preserves learner baseline competence matching.
  * **Error Frequency Proximity (15% weight):** Evaluates behavioral mistake recurrence over a bounded scale.

* **Adaptive Pedagogical Revision (`adapt_solution`):**  
  * **Remedial Escalation:** When a student repeats an error 4 or more times, difficulty switches to remedial mode and appends two extra scaffolded drills.
  * **Accelerated Track:** When an advanced student makes 1 or fewer errors, the pacing shifts to an accelerated mastery curriculum.
  * **Cross-Topic Scaffolding:** Dynamically annotates adapted guidance if matched across different subjects.

* **Dynamic Retention (`retain_case`):**  
  Converts each resolved problem-solution pair into a newly keyed case (e.g., `CASE-006`, `CASE-007`) and appends it to persistent active memory, enabling incremental learning without system retraining.

* **Terminal UI Engine:**  
  Features ANSI true-color box layouts, in-line ASCII affinity progress bars, and step-by-step telemetry logs.

---

## Interactive CLI Menu

The program provides an interactive terminal dashboard supporting live diagnosis and inspection:
1. **[1] Run Default Assessment Scenario:** Automatically evaluates the baseline test case (Algebra, Formula Misuse, Beginner, 5 errors).
2. **[2] Enter Custom Student Error (Solve & Retain):** Allows interactive prompt input for topic, error type, proficiency level, and error count, executing the full 4R cycle in real time.
3. **[3] View Entire Case Base Repository:** Displays all initial and newly learned cases within active memory.
4. **[4] Exit System:** Closes the tutoring environment.

---

## How to Run

1. Clone or download the repository to your local computer.
2. Open a terminal or VS Code in the project directory.
3. Run the script using Python:
   ```bash
   python its_cbr_system.py