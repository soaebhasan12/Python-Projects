# Password Generator

This project is a **Password Generator** built using Python. It allows users to create secure passwords by specifying the number of letters, numbers, and symbols they want in their password.

## Features

- **Customizable Password Composition**:
  - Users can specify the number of letters, numbers, and symbols in the password.
- **Two Levels of Password Generation**:
  - **Easy Level**: Generates a password by appending characters in sequence (commented out in the code).
  - **Hard Level**: Generates a password with shuffled characters for better security.

## How It Works

1. The program prompts the user to input:
   - The number of letters they want in their password.
   - The number of numbers they want in their password.
   - The number of symbols they want in their password.
2. The program generates a password based on the user's input:
   - Randomly selects characters from predefined lists of letters, numbers, and symbols.
   - Shuffles the characters for added security (in the hard level).
3. The generated password is displayed to the user.

## Example Output

Workspace
(rerun without)
Collecting workspace information

Here is a structured version of the readMe.md file for the Password Generator project:

Welcome to the PyPassword Generator! How many letters would you like in your password? 5 How many Integers would you like in your password? 3 How many symbols would you like in your password? 2 ['a', 'B', '3', '!', 'x', '7', 'y', '2', '@', 'z'] ['x', '3', 'y', 'z', 'B', '2', '!', '7', 'a', '@']

Your Password is: x3yzB2!7a@


## How to Run

1. Make sure you have Python installed on your system.
2. Navigate to the project directory.
3. Run the script `08_Create_a_Pasoword_Generator_PROJECT.PY` using Python:
   ```bash
   python 08_Create_a_Pasoword_Generator_PROJECT.PY