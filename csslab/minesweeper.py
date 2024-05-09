from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/minesweeper')
def display_minesweeper_game():
    return get_test_html()

def get_test_html():
    line1 = render_template("blank.html") + render_template("zero.html") + render_template("one.html")\
            + render_template("two.html") + render_template("three.html") + render_template("four.html")\
            + render_template("five.html") + render_template("six.html") + render_template("seven.html")\
            + render_template("eight.html") + render_template("flag.html")
    return render_template("head.html") + line1 + "<br>" + line1

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)