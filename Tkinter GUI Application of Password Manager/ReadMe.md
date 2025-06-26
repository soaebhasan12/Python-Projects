# Password Manager GUI App with Tkinter

This project is a simple Password Manager application built using Python's Tkinter library. It allows users to generate secure passwords, save them along with website and email/username information, and copy generated passwords to the clipboard for easy use.

## Features

- **Password Generation:**
  - Generates strong, random passwords containing letters, numbers, and symbols.
  - Passwords are automatically copied to the clipboard for convenience.

- **Data Storage:**
  - Saves website, email/username, and password entries to a local `data.txt` file.
  - Prompts the user to confirm before saving credentials.

- **User Interface:**
  - Clean and simple GUI built with Tkinter.
  - Includes input fields for website, email/username, and password.
  - Buttons for generating passwords and saving entries.
  - Displays a logo image at the top of the window.

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
1. Clone or download this repository.
2. Ensure `logo.png` is present in the project directory.
3. Run the main application:
   ```bash
   python main.py
   ```

## File Structure
- `main.py` — Main application file.
- `logo.png` — Logo image displayed in the GUI.
- `data.txt` — File where saved credentials are stored (created after first save).
- `Day-05 Password Generator/` and `staged solutions/` — Additional folders for exercises and solutions (not required for main app).

## Usage
1. Enter the website and email/username.
2. Click "Generate Password" to create a secure password.
3. Click "Add" to save the credentials. The app will prompt for confirmation before saving.
4. Saved credentials are appended to `data.txt` in the format:
   ```
   website | email | password
   ```

## License
This project is for educational purposes.
