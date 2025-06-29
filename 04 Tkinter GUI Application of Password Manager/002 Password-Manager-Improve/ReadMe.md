# Advanced Password Manager GUI App with Tkinter

Welcome to Day 30 of #100DaysOfCode! This project is an improved Password Manager built with Python's Tkinter, featuring advanced error handling and JSON-based data storage. Inspired by the need for safer, more reliable password management, this app now lets you save, search, and manage your credentials with confidence.

## Topics Covered on Day 30
- Errors and Exceptions in Python
- Try/Except/Else/Finally blocks
- FileNotFoundError and handling missing files
- Working with JSON: saving and loading data
- Data validation and user feedback in GUIs
- Improving user experience with robust error handling

## What's New in This Version?
- **Error & Exception Handling:**
  - Prevents app crashes by gracefully handling missing files and other common issues.
- **JSON Data Storage:**
  - Credentials are now stored in a structured `data.json` file, making it easier to manage and search your data.
- **Search Functionality:**
  - Instantly look up saved credentials by website name.
- **All Previous Features:**
  - Secure password generation, clipboard copy, and a user-friendly Tkinter interface.

## Features
- Generate strong, random passwords with one click
- Save website, email, and password securely in a JSON file
- Search for saved credentials by website
- User-friendly GUI with validation and helpful popups
- Robust error handling for a smooth experience

## Getting Started

### Prerequisites
- Python 3.x
- Required packages:
  - `tkinter` (usually included with Python)
  - `pyperclip` (for clipboard functionality)

Install `pyperclip` if not already installed:
```bash
pip install pyperclip
```

### Running the App
1. Ensure `logo.png` is present in the project directory.
2. Run the application:
   ```bash
   python main.py
   ```

## How It Works
- **Add Credentials:** Enter website, email, and password (or generate one), then click "Add". Data is saved in `data.json`.
- **Search Credentials:** Enter a website and click "Search" to retrieve your saved email and password.
- **Error Handling:** If the data file is missing or a website is not found, the app will notify you instead of crashing.

## Why JSON?
JSON is a widely-used data format for storing and transferring data. By using JSON, your password manager is more robust, portable, and ready for future enhancements.

## License
This project is for educational purposes and personal use.
