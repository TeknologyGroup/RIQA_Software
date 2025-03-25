const socket = io();

function sendToAI() {
    const input = document.getElementById('userInput').value;
    socket.emit('process_input', {text: input});
}

socket.on('ai_response', (data) => {
    document.getElementById('response').innerText = data.result;
});
