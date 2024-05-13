from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/minesweeper')
def display_minesweeper_game():
    return get_empty_grid_of_cells()

def get_characters_test_HTML():
    line1 = render_template("blank.html") + render_template("zero.html") + render_template("one.html")\
            + render_template("two.html") + render_template("three.html") + render_template("four.html")\
            + render_template("five.html") + render_template("six.html") + render_template("seven.html")\
            + render_template("eight.html") + render_template("flag.html")
    return render_template("head.html") + line1 + "<br>" + line1 + render_template("blank.html") + render_template("blank.html") + "<br>" + render_template("blank.html") + render_template("blank.html") + line1

def get_cell_click_test_HTML():
    return render_template("click_test.html")

# def create_blank_block_of_cells():
    # return '<div id="cell_grid" onLoad="instantiate_field()"></div>'

def get_empty_grid_of_cells():
    return render_template("minesweeper.html")

if __name__ == '__main__':
    my_port = 5113
    app.run(host='0.0.0.0', port = my_port)