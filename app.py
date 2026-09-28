from flask import Flask, render_template, request, jsonify
from config import EDUCATION_BOT_NAME

app = Flask(__name__)

FAQ = {
    "hello": f"Hi! I'm {EDUCATION_BOT_NAME}. I can help with study topics, homework guidance, and learning resources.",
    "hi": f"Hello! I'm {EDUCATION_BOT_NAME}. What subject would you like help with?",
    "math": "For Mathematics, I can explain topics such as algebra, geometry, percentages, and basic problem solving.",
    "python": "Python is a beginner-friendly programming language. Start with variables, data types, conditions, loops, functions, and lists.",
    "study": "Try a simple study routine: choose one topic, learn the concept, solve a few questions, review mistakes, and take a short break.",
    "exam": "For exam preparation, make a topic list, prioritize difficult areas, practice questions, and revise regularly.",
}

def get_response(message):
    text = message.lower().strip()

    for keyword, response in FAQ.items():
        if keyword in text:
            return response

    if any(word in text for word in ["thank", "thanks"]):
        return "You're welcome! Keep learning and practicing."

    return (
        "I can help with education-related questions. "
        "Try asking about Mathematics, Python, study tips, or exam preparation."
    )

@app.route("/")
def home():
    return render_template("index.html", bot_name=EDUCATION_BOT_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    if not message.strip():
        return jsonify({"reply": "Please type a question."})
    return jsonify({"reply": get_response(message)})

if __name__ == "__main__":
    app.run(debug=True)
