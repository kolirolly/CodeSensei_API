🚀 CodeSensei
CodeSensei is an AI-powered coding assistant that helps developers and non-programmers alike understand, generate, and explore code using natural language. Built with FastAPI and powered by Groq's blazing-fast language models, CodeSensei simplifies coding one prompt at a time.

🧠 Features
🔍 Explain Mode – Break down complex code into easy-to-understand explanations.

⚡ Generate Mode – Instantly generate code snippets or entire functions.

💬 Ask Mode – Ask any programming-related question and get meaningful responses.

🤖 Auto Mode – Intelligent, context-aware suggestions.

🌙 Light/Dark Theme – Switch between light and dark modes for comfortable coding.

💡 Clean UI – Minimal, modern interface designed for focus and productivity.

🛠️ Tech Stack

Layer	Tech
Frontend	HTML, CSS (custom styled), Vanilla JS
Backend	FastAPI
AI Engine	Groq API (Meta’s LLaMA 4 model)
Deployment	Localhost / Any hosting provider
⚙️ Getting Started
🔧 Backend Setup (FastAPI + Groq API)
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/CodeSensei.git
cd CodeSensei
Set up Python environment

bash
Copy
Edit
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI server

bash
Copy
Edit
uvicorn app.main:app --reload
🔐 Don't forget to add your Groq API key in a .env file or directly inside the groq_api.py.

🖥️ Frontend Setup (Vanilla HTML/CSS/JS)
Just open index.html in your browser. No build tools required!

Or serve it with a lightweight server:

bash
Copy
Edit
cd frontend
python -m http.server
📁 Project Structure
css
Copy
Edit
CodeSensei/
│
├── app/
│   ├── main.py
│   ├── groq_api.py
│   └── templates/
│       └──index.html
├── static/
├ └──style.css
├ └── app.js
├── requirements.txt
└── README.md
🖼️ Screenshots


📄 License
This project is licensed under the MIT License.

🙌 Acknowledgements
Groq

FastAPI

Meta LLaMA

[Vanilla JS + CSS] for fast and flexible UI

Crafted with 💙 for devs, by devs.
