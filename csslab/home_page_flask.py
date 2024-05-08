from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/minesweeper')
def display_minesweeper_game():
    return render_template("templates/minesweeper.html")

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)