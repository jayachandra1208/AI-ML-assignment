A full-stack web application that leverages the power of the GROQ API to provide various AI-driven functionalities, including generating follow-up questions, providing a transparency score for text, and generating a summary of the input.

This project is built with a lightweight Python Flask backend and a modern, responsive HTML/Tailwind CSS frontend. It is configured for easy local development and cloud deployment.

🌟 Features
Generate Follow-up Questions: Input any text, and the AI will generate 3-5 concise and relevant questions to explore the topic further.

Get Transparency Score: Analyze the clarity, completeness, and potential ambiguity of your text with a score from 1-10 and a detailed explanation.

Generate Summary: Get a quick, one-paragraph summary of any lengthy text you provide.

Responsive Design: The frontend is designed to be fully functional and visually appealing on all devices, from mobile phones to desktops.

API-First Architecture: A clean separation between the backend (API) and frontend (UI) allows for scalability and flexibility.

🚀 Technologies Used
Backend:

Python 3

Flask (Web Framework)

Gunicorn (Production WSGI Server)

requests (HTTP Library)

GROQ API (For LLM functionality)

Frontend:

HTML5

Tailwind CSS (For styling and responsive design)

JavaScript (For API calls and DOM manipulation)

📁 File Structure
/ai-ml-app
├── backend/
│   ├── app.py              # The Flask backend application
│   ├── requirements.txt    # Python dependencies
│   └── Procfile            # For deployment on platforms like Render
└── frontend/
    └── index.html          # The HTML frontend application

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

Create and activate a Python virtual environment:

Windows: python -m venv venv && venv\Scripts\activate

Install the required Python packages:

pip install -r requirements.txt

Obtain a GROQ API Key:

Go to GROQ website and create an API key.

Set the API Key as an Environment Variable:

This is the most secure way to manage your API key.


set GROQ_API_KEY="your_api_key_here"

Start the Flask server using Gunicorn:

gunicorn --bind 0.0.0.0:5000 app:app

The backend server will now be running on http://127.0.0.1:5000.

Step 3: Run the Frontend
Open the frontend/index.html file in your preferred web browser.

The frontend is a static page that will automatically connect to your running backend.

🚀 Deployment
The application is configured for deployment to a service like Render.

Backend: The Procfile and use of environment variables for the API key (os.environ.get("GROQ_API_KEY")) allow for easy deployment of the Flask service.

Frontend: The frontend directory contains all the static assets for a static site deployment.