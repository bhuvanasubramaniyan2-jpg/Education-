const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");

function addMessage(text, type) {
    const wrapper = document.createElement("div");
    wrapper.className = `message ${type}`;

    if (type === "bot") {
        wrapper.innerHTML = `
            <span class="avatar">🤖</span>
            <div class="bubble"></div>
        `;
    } else {
        wrapper.innerHTML = `<div class="bubble"></div>`;
    }

    wrapper.querySelector(".bubble").textContent = text;
    chatBox.appendChild(wrapper);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage(message) {
    addMessage(message, "user");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        addMessage(data.reply, "bot");
    } catch (error) {
        addMessage("Sorry, something went wrong. Please try again.", "bot");
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    input.value = "";
    await sendMessage(message);
    input.focus();
});

function sendSuggestion(message) {
    sendMessage(message);
}
