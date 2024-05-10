const grid_width = 20;
const grid_height = 10;

// grid of cells. each cell contains an object containing the cell's value along with a reference to the character that is displaying that cell
grid = new Array(grid_width * grid_height);

function instantiate_field() {
    console.log("called instantiate_field");
    cell_grid_div = document.getElementById("cell_grid");
    if (cell_grid_div === undefined) {
        console.log("Couldn't find grid");
        return;
    }
    console.log("found cell grid: "+cell_grid_div);
    for (y=0; y<grid_height; y++) {
        for (x=0; x<grid_width; x++) {
            new_cell_html = document.createElement("span");
            console.log("Created new HTML element: " + new_cell_html);
            value = Math.floor(Math.random() * 10);
            assign_symbol_and_colors_to_HTML_cell(value, new_cell_html);
            cell_grid_div.appendChild(new_cell_html);
            grid[x + y * grid_width] = {value: value, element: new_cell_html};
        }
        line_break = document.createElement("br");
        cell_grid_div.appendChild(line_break);
    }
}

is_red = true;
function assign_symbol_and_colors_to_HTML_cell(value, cell) {
    cell.innerHTML = value;
    cell.style.color = (is_red ? "red" : "blue");
    is_red = !is_red;
}

function display_coordinates_of_click(x, y) {
    display_paragraph = document.getElementById("coordinate_display");
    display_paragraph.innerHTML = x + ", " + y;
    incrementer += x + y;
    console.log("A letter was clicked: " + x + ", " + y);
    display_incrementer = document.getElementById("incrementer_display");
    display_incrementer.innerHTML = incrementer;
}