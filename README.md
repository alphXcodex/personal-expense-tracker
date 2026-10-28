# Personal Expense Tracker

A beginner-friendly command-line project built with Python. It stores your expenses locally in a JSON file, so the data remains available when you reopen the program.

## Features

- Add an expense with category, description, amount, and date
- View all saved expenses
- Calculate total spending
- See spending grouped by category
- Validate amounts, dates, and menu choices
- Save data locally in `expenses.json`

## Requirements

- Python 3.9 or newer (uses only Python's standard library)
- No extra packages are required

## Run the project

1. Download or clone this repository.
2. Open a terminal in this folder.
3. Run:

   ```bash
   python expense_tracker.py
   ```

   If your system uses `python3`, run:

   ```bash
   python3 expense_tracker.py
   ```

## How data is stored

Each expense is saved in `expenses.json`. Keep this file if you want to retain your data. The project uses local storage only; it does not send your data anywhere.

## Quick manual test

1. Choose `1` and add: category `Food`, description `Lunch`, amount `120`, and press Enter for today's date.
2. Choose `2` and confirm the expense appears.
3. Choose `3` and confirm the total is ₹120.00 (if this is your only entry).
4. Choose `4` and confirm `Food` shows ₹120.00.
5. Choose `5`, run the program again, and confirm the expense is still saved.

## Possible future improvements

- Delete or edit an expense
- Monthly reports
- Export to CSV
- A graphical user interface

## Learning goals

This project practices functions, loops, conditionals, lists, dictionaries, file handling, JSON, input validation, and basic error handling.
