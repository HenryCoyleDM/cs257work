function display_coordinates_of_click(x, y) {
    display_paragraph = document.getElementById("coordinate_display");
    display_paragraph.innerHTML = x + ", " + y;
    console.log("A letter was clicked: " + x + ", " + y);
}