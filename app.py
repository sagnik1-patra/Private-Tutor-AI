from flask import Flask, render_template, request, jsonify
import sys
sys.path.append(r"C:\Users\sagni\Downloads\Private-Tutor_AI")

# ✅ Import TutorAgent from notebook
import nbimporter
from Untitled1117 import TutorAgent

# 🌟 Initialize TutorAgent
tutor = TutorAgent()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    reply = tutor.handle_request(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
