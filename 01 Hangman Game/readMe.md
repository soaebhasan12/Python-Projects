 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   

# Hangman Game 🎮

This project is a Python implementation of the classic **Hangman Game**. The player guesses letters to uncover a hidden word, with a limited number of incorrect guesses allowed before the game ends.

## Features

- **Random Word Selection**: Words are randomly chosen from a predefined list in [`hangman_words.py`](hangman_words.py).
- **ASCII Art**: Visual representation of the hangman using ASCII art from [`hangman_art.py`](hangman_art.py).
- **User-Friendly Interface**: Displays the current progress of the word and provides feedback on repeated or incorrect guesses.
- **Win/Lose Conditions**: The game ends when the player either guesses the word correctly or runs out of lives.

## How to Play

1. Run the game by executing [`main.py`](main.py).
2. The program will randomly select a word, and you will see blanks representing the letters of the word.
3. Guess one letter at a time by typing it into the console.
4. If the guessed letter is in the word, it will be revealed in the correct position(s).
5. If the guessed letter is not in the word, you lose a life, and the hangman drawing progresses.
6. The game ends when:
   - You guess the entire word correctly (You win 🎉).
   - You run out of lives (You lose 😢).

## File Structure

- [`main.py`](main.py): The main game logic.
- [`hangman_words.py`](hangman_words.py): Contains the list of words for the game.
- [`hangman_art.py`](hangman_art.py): Contains ASCII art for the hangman stages and the game logo.

## Example Gameplay
Guess a letter: a You have guessed a, that's not in the word. You lose a life. 
=======
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=======

## Requirements

- Python 3.x

## How to Run

1. Clone this repository or download the files.
2. Open a terminal and navigate to the project directory.
3. Run the game using the following command:
   ```bash
   python main.py