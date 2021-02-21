window.onload = function() {
    document.getElementById("board-bar").onclick = function() {
        // Change arrow
        var arrow = document.getElementById("arrow");
        if (arrow.getAttribute("src") === "images/up.png") {
            arrow.src = "images/down.png";
        }
        else {
            arrow.src = "images/up.png";
        }

        // Change whiteboard
        var whiteboard = document.getElementById("whiteboard");
        whiteboard.classList.toggle("invisible");
        whiteboard.src = "https://awwapp.com/";
    }
}
