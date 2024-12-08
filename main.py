from flask import Flask, render_template, request, session
import random
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET'])
def show_game():
    # Generate a random number and store it in the session on first visit
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    return render_template('game.html', message=None)


@app.route('/guess', methods=['POST'])
def check_guess():

    # This route handles the player's guess
    guess = int(request.form.get('guess', 0))

    # Retrieve the random number from the session
    random_number = session.get('random_number')

    if guess == random_number:
        message = "Correct! You win! 🎉 A new number has been generated!"
        session['random_number'] = random.randint(1, 100)

    elif guess < random_number:
        message = "Too low! Try again! ⬆️"
    else:
        message = "Too high! Try again! ⬇️"

    return render_template('game.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)