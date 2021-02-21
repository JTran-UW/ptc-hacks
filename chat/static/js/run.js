window.onload = function() {
    document.getElementById("board-bar").onclick = function() {
        // Change arrow
        var arrow = document.getElementById("arrow");
        if (arrow.getAttribute("src") === "/static/images/up.png" || arrow.getAttribute("src") === "../static/images/up.png") {
            arrow.src = "../static/images/down.png";
        }
        else {
            arrow.src = "../static/images/up.png";
        }

        // Change whiteboard
        var whiteboard = document.getElementById("whiteboard");
        whiteboard.classList.toggle("invisible");
        whiteboard.src = "https://awwapp.com/";
    }
}
