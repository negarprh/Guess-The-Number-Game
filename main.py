from flask import Flask, render_template, request

app = Flask(__name__)

# Generate a random number when server starts
secret_number = 42


@app.route('/', methods=['GET'])
def show_game():
    # This route shows the game page
    return render_template('game.html')


@app.route('/guess', methods=['POST'])
def check_guess():
    # This route handles the player's guess
    guess = int(request.form.get('guess', 0))

    if guess == secret_number:
        message = "Correct! You win! 🎉"
    elif guess < secret_number:
        message = "Too low! Try again! ⬆️"
    else:
        message = "Too high! Try again! ⬇️"

    return render_template('game.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)