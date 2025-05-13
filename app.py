
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your actual API key

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    response = chat.send_message(user_input)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
