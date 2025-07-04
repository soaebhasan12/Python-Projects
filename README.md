# Quizzler App Final Project

This is a simple quiz application built with Python and Tkinter. It fetches True/False questions from the Open Trivia Database API and presents them in a graphical user interface.

## Features
- Fetches 10 random True/False questions from the internet.
- Interactive GUI using Tkinter.
- Instant feedback on answers (green/red background).
- Score tracking.
- End-of-quiz message and disables buttons when finished.

## How It Works
1. The app fetches questions from the Open Trivia Database API using the `requests` library.
2. Each question is displayed in the GUI, and the user selects True or False.
3. The app provides immediate feedback and updates the score.
4. When all questions are answered, the final score is shown and the quiz ends.

## File Structure
- `main.py`: Entry point; sets up the quiz and GUI.
- `data.py`: Fetches questions from the API.
- `question_model.py`: Defines the `Question` class.
- `quiz_brain.py`: Handles quiz logic and scoring.
- `ui.py`: Manages the Tkinter GUI.
- `images/`: Contains `true.png` and `false.png` for button icons.

## Requirements
- Python 3.x
- `requests` library
- Tkinter (usually included with Python)

## How to Clone This Repository
1. Open your terminal or command prompt.
2. Run the following command:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
3. Navigate into the project directory:
   ```bash
   cd your-repo-name
   ```

## How to Run
1. Make sure you have Python 3 installed.
2. Install the `requests` library if you don't have it:
   ```bash
   pip install requests
   ```
3. Place `true.png` and `false.png` images in an `images/` folder in the same directory as your scripts.
4. Run the app:
   ```bash
   python main.py
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits
- [Open Trivia Database](https://opentdb.com/) for quiz questions.
- Inspired by the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.
