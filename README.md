# ⌨️ typectl

**typectl** is a minimalist, fast, and customizable command-line typing trainer built entirely in Python. It allows you to test your typing speed directly in the terminal without relying on heavy web browsers, while saving your history locally to track your progress over time.

## ✨ Features

* **Strict & Fair Scoring:** Calculates WPM (Words Per Minute) and Accuracy by exclusively counting correctly typed words.
* **Smart Text Matching:** Case-insensitive and punctuation-forgiving accuracy checks. 
* **Local Stat Tracking:** Automatically saves all your test results to a local `history.json` file.
* **Lifetime Analytics:** Instantly view your highest speed, average WPM, and average accuracy across all tests.
* **Custom Practice Texts:** Pulls testing sentences dynamically from a customizable `words.txt` file, so you can practice with the vocabulary or code snippets of your choice.
* **Distraction-Free UI:** Uses ANSI terminal colors to highlight the target text for easy reading.

## 🚀 Usage

**typectl** is driven by a clean CLI interface. Open your terminal and use the following commands:

**Start a Typing Test**
```bash
python typectl.py test
