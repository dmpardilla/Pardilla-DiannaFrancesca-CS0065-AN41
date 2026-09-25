# Student Early Warning System - Academic Risk Classification

**Author:** Dianna Francesca M. Pardilla  
**Course & Section:** CS0065 / AN41  

---

## Overview
This repository contains the completed deliverable for **Asynchronous Activity 1**. The project develops an end-to-end predictive machine learning pipeline using **KNIME Analytics Platform** to identify and classify students at academic risk based on core performance indicators.

## Repository Contents
- `Pardilla-DemoEarlyWarningTool-MP1.knwf` — The exported KNIME workflow featuring data preprocessing, normalization, partitioning, model training, and performance scoring.
- `student_performance_knime.csv` — The academic dataset containing student performance metrics across coursework and examinations.
- `Pardilla-Dianna-Francesca-Machine-Problem-1-Evidence.pdf` — Comprehensive step-by-step verification document showcasing terminal command executions, node configurations, and evaluation matrices.

## Evaluated Machine Learning Algorithms
- **Decision Tree Classifier:** Utilizes Gini index splitting criteria to establish non-linear decision boundaries for risk categories.
- **Logistic Regression:** Normalized classification model optimized with a SAG solver to assess relative class probabilities.
- **Random Forest Ensemble:** Multi-tree bagging ensemble designed to reduce variance and optimize classification stability.

## Execution Instructions
1. Download or clone this repository to your local workspace.
2. Open **KNIME Analytics Platform** and select **File** -> **Import KNIME Workflow...** to load `Pardilla-DemoEarlyWarningTool-MP1.knwf`.
3. Open the **CSV Reader** node configuration and link the file path to `student_performance_knime.csv`.
4. Run all pipeline nodes (**Execute All**).
5. Inspect the output views of the **Scorer** nodes to analyze the confusion matrices, accuracy statistics, and predictive metrics.