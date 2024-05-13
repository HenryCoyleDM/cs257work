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
    for (y=0; y<grid_height; y++) {
        for (x=0; x<grid_width; x++) {
            // https://www.w3schools.com/jsref/met_node_appendchild.asp
            new_cell_html = document.createElement("span");
            // console.log("Created new HTML element: " + new_cell_html);
            value = Math.floor(Math.random() * 12);
            assign_symbol_and_colors_to_HTML_cell(value, new_cell_html, x, y);
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
                             '<span class="flag">!</span>']

                             // flag symbol: &#x2691, unfortunately not monospaced

function assign_symbol_and_colors_to_HTML_cell(value, cell, x, y) {
    // https://www.w3docs.com/snippets/javascript/how-to-create-a-new-dom-element-from-html-string.html
    template = document.createElement('template');
    template.innerHTML = cell_text_templates[value];
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
    template_clone = template.content.children[0];
    console.log("Created a template: "+template_clone);
    cell.innerHTML = template_clone.innerHTML;
    // https://stackoverflow.com/questions/2221160/how-to-change-a-css-class-style-through-javascript
    cell.className = template_clone.className;
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

function cell_is_clicked(x, y, event) {
    // https://stackoverflow.com/questions/2405771/is-right-click-a-javascript-event
    var is_ctrl_key_pressed;
    // console.log(event);
    is_ctrl_key_pressed = event.ctrlKey;
    console.log((is_ctrl_key_pressed ? "Control clicked (" : "Clicked (")+x+", "+y+")");
}