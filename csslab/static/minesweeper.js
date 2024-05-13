const grid_width = 20;
const grid_height = 10;

// grid of cells. each cell contains an object containing the cell's value along with a reference to the character that is displaying that cell
grid = new Array(grid_width * grid_height);

function instantiate_field() {
    // console.log("called instantiate_field");
    cell_grid_div = document.getElementById("cell_grid");
    if (cell_grid_div === undefined) {
        console.log("Couldn't find grid");
        return;
    }
    // console.log("found cell grid: "+cell_grid_div);
    grid_of_bombs = get_random_distribution_of_bombs();
    for (y=0; y<grid_height; y++) {
        for (x=0; x<grid_width; x++) {
            // https://www.w3schools.com/jsref/met_node_appendchild.asp
            new_cell_html = document.createElement("span");
            // console.log("Created new HTML element: " + new_cell_html);
            value = grid_of_bombs[x + grid_width * y];
            assign_symbol_and_colors_to_HTML_cell(value, new_cell_html);
            assign_click_function_to_HTML_cell(new_cell_html, x, y);
            cell_grid_div.appendChild(new_cell_html);
            grid[x + y * grid_width] = {value: value, element: new_cell_html};
        }
        line_break = document.createElement("br");
        cell_grid_div.appendChild(line_break);
    }
}

// HTML strings representing the symbology for each value of a cell
const cell_text_templates = ['<span class="zero">&nbsp</span>',
                             '<span class="one">1</span>',
                             '<span class="two">2</span>',
                             '<span class="three">3</span>',
                             '<span class="four">4</span>',
                             '<span class="five">5</span>',
                             '<span class="six">6</span>',
                             '<span class="seven">7</span>',
                             '<span class="eight">8</span>',
                             '<span class="blank">&#x2588</span>',
                             '<span class="blank">&#x2588</span>',
                             '<span class="flag">!</span>',
                             '<span class="flag">!</span>']

                             // flag symbol: &#x2691, unfortunately not monospaced

function assign_symbol_and_colors_to_HTML_cell(value, cell) {
    // https://www.w3docs.com/snippets/javascript/how-to-create-a-new-dom-element-from-html-string.html
    template = document.createElement('template');
    template.innerHTML = cell_text_templates[value];
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
    template_clone = template.content.children[0];
    cell.innerHTML = template_clone.innerHTML;
    // https://stackoverflow.com/questions/2221160/how-to-change-a-css-class-style-through-javascript
    cell.className = template_clone.className;
}

function assign_click_function_to_HTML_cell(cell, x, y) {
    // https://www.w3schools.com/jsref/event_onclick.asp
    cell.onclick = function(event) {
        cell_is_clicked(x, y, event);
    }
}

function display_coordinates_of_click(x, y) {
    display_paragraph = document.getElementById("coordinate_display");
    display_paragraph.innerHTML = x + ", " + y;
    incrementer += x + y;
    console.log("A letter was clicked: " + x + ", " + y);
    display_incrementer = document.getElementById("incrementer_display");
    display_incrementer.innerHTML = incrementer;
}

const UNEXPLORED = 9;
const BOMB = 10;
const FLAG = 11;
const INCORRECT_FLAG = 12;

function cell_is_clicked(x, y, event) {
    // https://stackoverflow.com/questions/2405771/is-right-click-a-javascript-event
    var is_ctrl_key_pressed;
    // console.log(event);
    is_ctrl_key_pressed = event.ctrlKey;
    // console.log((is_ctrl_key_pressed ? "Control clicked (" : "Clicked (")+x+", "+y+")");
    cell_value = get_cell_value(x, y);
    if (is_ctrl_key_pressed) {
        if (cell_value == FLAG) {
            set_cell_value_and_update_colors(x, y, BOMB);
        } else if (cell_value == INCORRECT_FLAG) {
            set_cell_value_and_update_colors(x, y, UNEXPLORED);
        } else {
            set_cell_value_and_update_colors(x, y, FLAG);
        }
    } else {
        if (cell_value == UNEXPLORED) {
            neighboring_bombs = get_number_of_neighboring_bombs(x, y);
            set_cell_value_and_update_colors(x, y, neighboring_bombs);
        } else if (cell_value == BOMB) {
            lose();
        } else if (cell_value >= 1 && cell_value <= 7) {
            if (cell_value == get_number_of_neighboring_flags(x, y)) {
                uncover_all_neighboring_cells(x, y);
            }
        }
    }
}

function set_cell_value_and_update_colors(x, y, new_value) {
    grid[x + grid_width * y].value = new_value;
    assign_symbol_and_colors_to_HTML_cell(new_value, grid[x + grid_width * y].element, x, y);
    console.log("Changing symbol at ("+x+", "+y+") to "+new_value);
}

function get_number_of_neighboring_bombs(x, y) {
    total = 0;
    for (i = x-1; i <= x+1; i++) {
        for (j = y-1; j <= y+1; j++) {
            if (is_in_bounds(i, j) && (i != x || j != y)) {
                test_value = get_cell_value(i, j);
                if (test_value == BOMB || test_value == FLAG) {
                    total++;
                }
            }
        }
    }
    return total;
}

function get_number_of_neighboring_flags(x, y) {
    total = 0;
    for (i = x-1; i <= x+1; i++) {
        for (j = y-1; j <= y+1; j++) {
            if (is_in_bounds(i, j) && (i != x || j != y)) {
                test_value = get_cell_value(i, j);
                if (test_value == FLAG || test_value == INCORRECT_FLAG) {
                    total++;
                }
            }
        }
    }
    return total;
}

function get_cell_value(x, y) {
    return grid[x + grid_width * y].value;
}

function is_in_bounds(x, y) {
    return x >= 0 && x < grid_width && y >= 0 && y < grid_height;
}

const number_of_bombs = 20;

function get_random_distribution_of_bombs() {
    grid_of_bombs = new Array(grid_width * grid_height);
    grid_of_bombs.fill(UNEXPLORED);
    for (i = 0; i < number_of_bombs; i++) {
        found_a_valid_position = false;
        while (!found_a_valid_position) {
            random_position = Math.floor(Math.random() * grid_width * grid_height);
            if (grid_of_bombs[random_position] == UNEXPLORED) {
                grid_of_bombs[random_position] = BOMB;
                found_a_valid_position = true;
            }
        }
    }
    return grid_of_bombs;
}

function lose() {
    alert("BOOM!");
}

function uncover_all_neighboring_cells(x, y) {
    console.log("Mass excavating at ("+x+", "+y+")");
    for (i = x-1; i <= x+1; i++) {
        for (j = y-1; j <= y+1; j++) {
            if (is_in_bounds(i, j) && (i != x || j != y)) {
                test_value = get_cell_value(i, j);
                console.log("Testing ("+i+", "+j+") for mass excavation. Its value is "+test_value);
                if (test_value == BOMB) {
                    lose();
                } else if (test_value == UNEXPLORED) {
                    neighboring_bombs = get_number_of_neighboring_bombs(i, j);
                    console.log("Uncovering cell ("+i+", "+j+"). There are "+neighboring_bombs+" neighboring bombs")
                    set_cell_value_and_update_colors(i, j, neighboring_bombs);
                }
            }
        }
    }
}