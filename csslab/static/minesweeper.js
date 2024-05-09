incrementer = 0;

function display_coordinates_of_click(x, y) {
    display_paragraph = document.getElementById("coordinate_display");
    display_paragraph.innerHTML = x + ", " + y;
    incrementer += x + y;
    console.log("A letter was clicked: " + x + ", " + y);
    display_incrementer = document.getElementById("incrementer_display");
    display_incrementer.innerHTML = incrementer;
}