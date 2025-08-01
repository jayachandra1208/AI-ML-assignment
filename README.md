AI/ML Explorer
A full-stack web application that leverages the power of the GROQ API to provide various AI-driven functionalities, including generating follow-up questions, providing a transparency score for text, and generating a summary of the input.

This project is built with a lightweight Python Flask backend and a modern, responsive HTML/Tailwind CSS frontend. It is configured for easy local development and cloud deployment.

🌟 Feature List
Generate Follow-up Questions: Dynamically creates 3-5 concise, relevant questions based on your input text.

Get Transparency Score: Analyzes your text for clarity and completeness, providing a score from 1 to 10 with a detailed explanation.

Generate Summary: Provides a one-paragraph summary of any text you provide.

Responsive Design: The application's interface is designed to work seamlessly on all devices, from mobile phones to desktops.

Separated Architecture: Built with a distinct frontend and a production-ready backend, allowing for easy maintenance and scalability.

💻 Getting Started
Follow these steps to set up and run the application on your local machine.

Prerequisites
Python 3.8+ installed

A code editor (e.g., VS Code)

Git (optional, but recommended)

Step 1: Clone the Repository
If you haven't already, clone the project from your GitHub repository.

git clone <your-github-repo-url>
cd ai-ml-app

Step 2: Set up the Backend
Navigate to the backend directory:

cd backend

Create and activate a Python virtual environment (recommended):

macOS/Linux: python -m venv venv && source venv/bin/activate

Windows: python -m venv venv && venv\Scripts\activate

Install the required Python packages:

pip install -r requirements.txt

Obtain a GROQ API Key:

Go to GroqCloud and create an API key.

Set the API Key as an Environment Variable:

This is the most secure way to manage your API key.

macOS/Linux:

export GROQ_API_KEY="your_api_key_here"

Windows:

set GROQ_API_KEY="your_api_key_here"

Start the Flask server using Gunicorn:

gunicorn --bind 0.0.0.0:5000 app:app

The backend server will now be running on http://127.0.0.1:5000.

Step 3: Run the Frontend
Open the frontend/index.html file in your preferred web browser.

The frontend is a static page that will automatically connect to your running backend.

📄 AI Service Documentation
The backend exposes three REST API endpoints, each with a single purpose.

Endpoint 1: Generate Follow-up Questions

Method: POST

URL: /generate-questions

Request Body: {"input": "Your text here."}

Response: {"questions": ["Question 1", "Question 2", ...]}

Description: Generates a list of questions based on the provided input.

Endpoint 2: Get Transparency Score

Method: POST

URL: /transparency-score

Request Body: {"input": "Your text here."}

Response: {"analysis": "Score: [Score]/10\nExplanation: [Detailed explanation]"}

Description: Analyzes text for clarity and completeness, providing a numerical score and a brief justification.

Endpoint 3: Generate Summary

Method: POST

URL: /generate-summary

Request Body: {"input": "Your text here."}

Response: {"summary": "A one-paragraph summary of the text."}

Description: Creates a concise summary of the provided text.

📝 Sample Product Entry + Example Report
Input Text:
The Q4 project plan is to launch a new product line with a focus on user experience and scalability. The team has allocated a budget of $500,000 and a six-month timeline, with a core team of 10 engineers.

Generated Report:

Follow-up Questions:

What specific features will be included in the new product line to enhance the user experience?

How will "scalability" be measured and what specific technologies will be used to achieve it?

How is the $500,000 budget allocated across different phases of the project?

What are the key milestones within the six-month timeline?

Transparency Score Analysis:

Score: 8/10

Explanation: The plan is transparent in its core objectives, budget, and timeline. However, it lacks specifics on the execution strategy, such as key milestones and the technologies used for scalability, which could improve its clarity.

Summary:
The Q4 project plan involves launching a new product line within a six-month timeline and a $500,000 budget. The initiative, led by a team of 10 engineers, will prioritize enhancing user experience and ensuring the product is scalable.

Reflection
I used AI tools as a collaborator throughout development, leveraging them to write initial code, debug issues like CORS, and draft project documentation. This freed me to focus on the high-level architecture and deployment process.

The project's design was guided by the principle of separation of concerns. The backend was a lightweight Flask microservice handling all AI logic, while the frontend was a simple, responsive HTML page dedicated to the user interface. This modular approach makes the application easy to deploy and scale.

For product transparency, the "Transparency Score" feature was a deliberate choice. It demonstrates how AI can be used to analyze its own output, providing a window into its reasoning. This was an essential part of the design, aimed at building user trust and providing insight into the AI's capabilities.
