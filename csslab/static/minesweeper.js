function display_coordinates_of_click() {
    display_paragraph = document.getElementById("coordinate_display");
    display_paragraph.innerHTML = Math.random() + ", " + Math.random();
    console.log("A letter was clicked");
}