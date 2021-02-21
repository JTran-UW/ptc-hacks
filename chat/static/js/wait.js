const chatSocket = new WebSocket(
    "ws://"
    + window.location.host
    + "/ws/chat/"
    + subject
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.getElementById("message").value = "Partner found!";
}

chatSocket.onclose = function(e) {
    console.error("Chat socket closed unexpectedly");
}

window.onload = function() {
    chatSocket.send(JSON.stringify({
        "message": "TEST"
    }));
}
