from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample chatbot response logic
def chatbot_response(user_message):
    # Simple hardcoded response logic (could be replaced with a chatbot model)
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm doing great! How about you?",
        "bye": "Goodbye! Have a nice day!"
    }
    return responses.get(user_message.lower(), "Sorry, I didn't understand that.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = chatbot_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

