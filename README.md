# Guess The Number Game 🔢

## Overview
"Guess The Number Game" is a web-based number guessing game created with Flask. The game generates a random number between 1 and 100, and the player tries to guess it. After each guess, the app provides feedback to guide the player toward the correct answer.

## Features
- Random number generation between 1 and 100
- Feedback on whether the guess is too high, too low, or correct
- Minimalistic UI for an enjoyable and distraction-free experience

## Project Structure
- `main.py`: The main Flask application file that handles the game logic and routes
- `templates/game.html`: HTML file for the main game interface
- `requirements.txt`: List of dependencies needed to run the project

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/guess_the_number_game.git
   cd guess_the_number_game
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to play the game.

## Screenshots
![Screenshot of Guess the Number Game](websiteScreenshot.png)

## Usage
1. Enter a number between 1 and 100.
2. Click "Submit Guess" to check your answer.
3. Keep guessing based on the feedback until you find the correct number!

## Future Improvements
- Add difficulty levels (e.g., change range based on difficulty)
- Add a scoring system to track number of attempts
- Improve styling and add animations

## License
This project is licensed under the MIT License.
