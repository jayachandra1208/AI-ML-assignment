
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests
import time
import os # Import the os module to access environment variables

app = Flask(__name__)
# FIX: Configure CORS to allow requests from all origins with a wildcard.
CORS(app, resources={r"/*": {"origins": "*"}})

# The base URL for the GROQ API.
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Get the API key from an environment variable for production security.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def call_groq_api(prompt, max_retries=5, initial_delay=1):
    """
    Calls the GROQ API with exponential backoff to handle rate limiting.
    """
    if not GROQ_API_KEY:
        return "An API error occurred: API key is missing. Please set the GROQ_API_KEY environment variable."

    for i in range(max_retries):
        try:
            headers = {
                'Authorization': f'Bearer {GROQ_API_KEY}',
                'Content-Type': 'application/json'
            }
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "model": "llama3-8b-8192" # You can choose a different model if you prefer
            }
            
            response = requests.post(
                GROQ_API_URL,
                headers=headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            result = response.json()

            if result.get("choices"):
                generated_text = result["choices"][0]["message"]["content"]
                return generated_text.strip()
            return "Could not generate content."
        except requests.exceptions.RequestException as e:
            if response.status_code == 429 and i < max_retries - 1:
                delay = initial_delay * (2 ** i)
                time.sleep(delay)
            else:
                return f"An API error occurred: {e}"
    return "Failed to get a response from the API after multiple retries."

@app.route('/generate-questions', methods=['POST'])
def generate_questions():
    """
    Endpoint to dynamically generate follow-up questions based on user input.
    """
    data = request.json
    user_input = data.get('input', '')

    if not user_input:
        return jsonify({"error": "Input text is required"}), 400

    prompt = f"Given the following user input, generate 3-5 concise and relevant follow-up questions. Format the output as a numbered list.\n\nUser Input: {user_input}"
    
    generated_questions = call_groq_api(prompt)

    if generated_questions.startswith("An API error occurred"):
        return jsonify({"error": generated_questions}), 500
    
    return jsonify({"questions": generated_questions.split('\n')})

@app.route('/transparency-score', methods=['POST'])
def transparency_score():
    """
    Endpoint to provide a 'transparency score' or validation logic.
    """
    data = request.json
    user_input = data.get('input', '')

    if not user_input:
        return jsonify({"error": "Input text is required"}), 400

    prompt = f"Analyze the following text for clarity, completeness, and potential ambiguity. Provide a transparency score from 1 to 10, where 10 is most transparent. Then, provide a brief, one-paragraph explanation for the score. Format your response like this: \n\nScore: [Your Score]/10\nExplanation: [Your detailed explanation]\n\nText to analyze: {user_input}"
    
    analysis_result = call_groq_api(prompt)

    if analysis_result.startswith("An API error occurred"):
        return jsonify({"error": analysis_result}), 500
    
    return jsonify({"analysis": analysis_result})

@app.route('/generate-summary', methods=['POST'])
def generate_summary():
    """
    Endpoint to generate a concise summary of the input text using GROQ.
    """
    data = request.json
    user_input = data.get('input', '')

    if not user_input:
        return jsonify({"error": "Input text is required"}), 400

    prompt = f"Provide a one-paragraph summary of the following text:\n\nText: {user_input}"
    
    summary_result = call_groq_api(prompt)

    if summary_result.startswith("An API error occurred"):
        return jsonify({"error": summary_result}), 500
    
    return jsonify({"summary": summary_result})

if __name__ == '__main__':
    if GROQ_API_KEY:
        app.run(debug=True, port=5000)
    else:
        print("Please set the GROQ_API_KEY environment variable to run locally.")
