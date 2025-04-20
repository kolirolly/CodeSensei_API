// Function to toggle the active button
const buttons = document.querySelectorAll('.button');
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        buttons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');
    });
});

// Clear the input field when "Clear" button is clicked
const clearButton = document.querySelector('.clear-btn');
clearButton.addEventListener('click', () => {
    document.querySelector('.input-field').value = '';
});

// Add a new message on button click (simulating send)
const sendButton = document.querySelector('.send-btn');
sendButton.addEventListener('click', () => {
    const inputField = document.querySelector('.input-field');
    const userInput = inputField.value;

    if (userInput.trim()) {
        // Create a new chat bubble for user input
        const newBubble = document.createElement('div');
        newBubble.classList.add('chat-bubble');
        newBubble.classList.add('user');
        
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.innerHTML = `<p>${userInput}</p>`;
        
        newBubble.appendChild(messageDiv);
        
        const chatContainer = document.querySelector('.chat-container');
        chatContainer.appendChild(newBubble);
        
        // Clear input field after sending
        inputField.value = '';
    }
});
