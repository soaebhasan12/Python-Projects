# Flashy Flash Card App

A capstone project for Day 31 of #DaysOfCode. This app helps you study the most frequently used words in a language using flashcards.

## Features
- Learn French vocabulary with English translations
- Flashcard interface with front (French) and back (English)
- Cards flip automatically after 3 seconds
- Mark words as known to remove them from the deck
- Progress is saved between sessions (words you know are not shown again)
- Beautiful UI using Tkinter and images

## How It Works
- The app loads a list of French words and their English translations from `data/french_words.csv`.
- When you mark a word as known, it is removed from your learning list and saved to `data/words_to_learn.csv`.
- If you make a mistake or want to review, unknown words remain in the deck.

## Getting Started
1. **Install requirements**: This app uses only standard Python libraries and pandas. Install pandas if you don't have it:
   ```sh
   pip install pandas
   ```
2. **Run the app**:
   ```sh
   python main.py
   ```
3. **Use the UI**:
   - Click the checkmark if you know the word (removes it from the deck)
   - Click the cross if you don't know the word (keeps it in the deck)

## File Structure
- `main.py` — Main application code
- `data/french_words.csv` — List of French words and English translations
- `data/words_to_learn.csv` — Progress file (auto-generated)
- `images/` — Card and button images

## Credits
- Frequency word lists: [HermitDave on GitHub](https://github.com/hermitdave/FrequencyWords)
- Images and starter data provided by the course

## License
This project is for educational purposes as part of #DaysOfCode.
