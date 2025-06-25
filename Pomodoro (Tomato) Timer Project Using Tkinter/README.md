# Pomodoro Timer Project (Tkinter)

A simple Pomodoro Timer application built with Python and Tkinter. This project helps you manage your work and break intervals using the Pomodoro Technique, which alternates focused work sessions with short and long breaks.

## Features
- Start, pause, and reset the timer
- Visual countdown display
- Automatic switching between work and break intervals
- Checkmarks to track completed work sessions
- Customizable colors and fonts

## How It Works
- **Work Session:** Default 1 minute (for demonstration; adjust as needed)
- **Short Break:** 5 minutes
- **Long Break:** 20 minutes
- After every 4 work sessions, a long break is triggered
- The timer and session type are displayed in the UI

## Getting Started

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python)

### Setup
1. Clone or download this repository.
2. Ensure `tomato.png` is in the same directory as `main.py`.
3. Run the application:
   ```bash
   python main.py
   ```

## File Structure
- `main.py` - Main application file
- `tomato.png` - Image used in the timer UI
- `staged_solutions/` - Stepwise solution files for learning

## Usage
- Click **Start** to begin the timer.
- Click **Reset** to stop and reset the timer and checkmarks.
- The timer will automatically switch between work and break intervals.

## Customization
- You can adjust the timer durations by changing the `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` constants in `main.py`.

## License
This project is for educational purposes.

---

**Pomodoro Technique:**
The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.
