// ================================
// CONFIG
// ================================
const API_URL = "http://localhost:8001/chat"; // FastAPI endpoint
const session_id = "user_" + Math.floor(Math.random() * 10000);


// ================================
// TOGGLE CHAT WINDOW (With Animation)
// ================================
function toggleChat() {
  const chat = document.getElementById("chatContainer");

  // Close chat
  if (chat.classList.contains("show")) {
    chat.classList.remove("show");

    setTimeout(() => {
      chat.style.display = "none";
    }, 300);

  }
  // Open chat
  else {
    chat.style.display = "flex";

    setTimeout(() => {
      chat.classList.add("show");
    }, 10);
  }
}


// ================================
// ADD MESSAGE TO CHAT BOX
// ================================
function appendMessage(role, text) {
  const box = document.getElementById("chatBox");
  const msg = document.createElement("div");

  // ✅ Convert \n to <br> so lines display correctly
  const formattedText = text.replace(/\n/g, "<br>");

  msg.innerHTML = `<strong>${role}:</strong><br>${formattedText}`;
  msg.style.margin = "6px 0";

  box.appendChild(msg);

  // Auto scroll
  box.scrollTop = box.scrollHeight;
}


// ================================
// SEND MESSAGE TO BACKEND
// ================================
async function sendMessage() {

  const input = document.getElementById("userInput");
  const text = input.value.trim();

  // Empty input check
  if (!text) return;

  // Show user message
  appendMessage("You", text);

  // Clear input
  input.value = "";

  // Show typing indicator
  const typingMsg = document.createElement("div");
  typingMsg.id = "typing";
  typingMsg.innerHTML = "<strong>Bot:</strong> Typing...";
  document.getElementById("chatBox").appendChild(typingMsg);


  try {

    // Send request
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        session_id: session_id,
        message: text
      })
    });

    // Server error check
    if (!response.ok) {
      throw new Error("Server Error: " + response.status);
    }

    // Get JSON
    const data = await response.json();

    console.log("Backend Response:", data); // Debug


    // Remove typing indicator
    const typing = document.getElementById("typing");
    if (typing) typing.remove();


    // Get reply safely
    const botReply =
      data.reply ||
      data.response ||
      data.message ||
      data.output ||
      "No reply from server";


    // Show bot message
    appendMessage("Bot", botReply);

  }

  catch (error) {

    console.error("Fetch Error:", error);

    // Remove typing if exists
    const typing = document.getElementById("typing");
    if (typing) typing.remove();

    appendMessage("Bot", "⚠️ Server not responding. Please try again.");

  }
}


// ================================
// AUTO OPEN CHAT (Optional)
// ================================
// Uncomment if you want auto-open on load
// window.onload = () => {
//   toggleChat();
// };
