from flask import Flask, request, jsonify
import openai
import os

from gpt4 import summarize_terms_of_service

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/api/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    terms_of_service_url = data["terms_of_service_url"]
    user_message = data["user_message"]

    summary, safety_remark = summarize_terms_of_service(terms_of_service_url, user_message)

    return jsonify({"summary": summary, "safety_remark": safety_remark})

if __name__ == "__main__":
    app.run()