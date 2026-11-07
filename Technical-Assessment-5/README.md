# Technical Assessment 5: Natural Language Processing & Sentiment Analysis Systems

**Authors:** Dianna Francesca M. Pardilla & Justin D. Vergara (Group: JustDia)  
**Course & Section:** CS054 (Intelligent Systems) / AN41  
**Date:** November 8, 2026  
**Professor:** Ms. Crisola G. Tan  

---

## Overview

This repository contains the complete laboratory implementation and documentation for **Technical Assessment 5: Sentiment Analysis** in Python.

The project explores Natural Language Processing (NLP) techniques to determine the sentiment, polarity, and emotional tone of text inputs. It demonstrates two distinct computational approaches: an API-driven continuous polarity evaluator utilizing Python's `TextBlob` library, and a custom lexical matching engine operating on dictionary datasets. Both applications feature interactive command-line menus, literary preset evaluation modes, detailed token diagnostic outputs, and formatted batch metrics summaries.

---

## Repository Contents

* **`LabAct5.py`** — Interactive script implementing **VibeCheck 3000**, an Object-Oriented TextBlob sentiment inspector. It includes interactive menu navigation (manual batch entry, pre-loaded literary quotes, and single-sentence quick checks), polarity categorization, mean score computation, and visual terminal bar chart summaries.
* **`Challenge5.py`** — Custom sentiment engine implementing **LexiMood: The Happy vs. Sad Word Showdown**. It performs regular expression tokenization against loaded happy and sad vocabulary datasets to determine overall sentence tone while highlighting specific matched terms.
* **`TA5_AN41_Pardilla, Vergara.pdf`** — The primary submission document containing the complete theoretical background, learning outcomes, complete source code listings, terminal execution logs, VS Code code screenshots, and academic references.

---

## Features & Implementation Details

* **Object-Oriented Architecture (`VibeCheckInspector`)**: Encapsulates sentiment evaluation logic within a modular class structure, tracking batch execution states, polarity score arrays, and automated aggregate distribution calculations.
* **TextBlob Polarity Scoring & Categorization**: Evaluates continuous polarity floating-point values $[-1.0, +1.0]$ to classify text into discrete sentiment tags (`Negative` for $p < 0$, `Neutral` for $p = 0$, and `Positive` for $0 < p \le 1$).
* **Regex-Based Tokenization (`_extract_tokens`)**: Employs normalized regular expression matching (`re.findall(r'\b[a-z]+\b', text.lower())`) to strip punctuation, convert characters to lowercase, and extract clean alphabetic tokens for precise text analysis.
* **High-Performance Lexical Lookups**: Utilizes hash-set structures (`HAPPY_LEXICON` and `SAD_LEXICON`) to perform $O(1)$ constant-time lookup operations within `number_happy(sentence)` and `number_sad(sentence)` counting functions.
* **Interactive Menu Systems & Diagnostic Reporting**: Provides menu-driven CLI options alongside built-in literary classic presets (e.g., J.R.R. Tolkien, Charles Dickens, Jane Austen) and detailed terminal visual distribution charts (`█`) for intuitive user interaction.

---

## Operating Instructions & How to Run

### 1. Prerequisites & Dependencies Installation

Ensure Python 3.x is installed on your system. Before running the scripts, install `textblob` and download its required NLTK corpora data via your terminal / PowerShell:

```bash
# Install TextBlob library
python -m pip install textblob

# Download required NLTK corpora
python -m textblob.download_corpora
```

> **Note for VS Code Users:** If using a specific Python interpreter environment, execute the command specifying the full binary path:
> ```powershell
> & 'C:\Users\<YourUser>\AppData\Local\Python\pythoncore-3.14-64\python.exe' -m pip install textblob
> & 'C:\Users\<YourUser>\AppData\Local\Python\pythoncore-3.14-64\python.exe' -m textblob.download_corpora
> ```

---

### 2. Operating `LabAct5.py` (VibeCheck 3000)

1. Open your terminal or VS Code Integrated Terminal (`Ctrl` + `` ` ``).
2. Navigate to the project directory:
   ```bash
   cd path/to/repository
   ```
3. Run the script:
   ```bash
   python LabAct5.py
   ```
4. **Interactive Menu Navigation:**
   * Enter `1`: Prompt user to input 10 custom sentences sequentially. Generates a final aggregate summary with percentages and bar charts.
   * Enter `2`: Automatically evaluates 10 pre-loaded literary classic quotes (J.R.R. Tolkien, Emily Brontë, Charles Dickens, etc.) and prints batch statistics.
   * Enter `3`: Performs a single-sentence quick sentiment polarity test.
   * Enter `4`: Exits the application.

---

### 3. Operating `Challenge5.py` (LexiMood)

1. Open your terminal or VS Code Integrated Terminal.
2. Run the script:
   ```bash
   python Challenge5.py
   ```
3. **Interactive Menu Navigation:**
   * Enter `1`: Prompt user to enter any custom text. Performs token extraction, counts happy/sad vocabulary matches, lists matched words, and outputs the overall tone.
   * Enter `2`: Allows testing against preset literary quotes (Happy Dominant, Sad Dominant, or Neutral/Tie).
   * Enter `3`: Displays all 35 happy words and 30 sad words currently loaded in the lexicon dataset.
   * Enter `4`: Exits the application.