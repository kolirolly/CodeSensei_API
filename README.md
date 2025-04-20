# 💻 CodeSensei

**CodeSensei** is an AI-powered coding assistant built using FastAPI and Groq's language models. It helps developers and non-programmers alike write, understand, and explore code using natural language. Whether you're debugging, learning a new concept, or generating boilerplate code — CodeSensei is your go-to companion.

---

## ✨ Features

- 🔍 **Explain Mode** – Understand complex code in plain English.
- ⚡ **Generate Mode** – Instantly generate code snippets or entire functions.
- 💬 **Ask Mode** – Ask anything related to programming concepts or syntax.
- 🤖 **Auto Mode** – Smart suggestions based on input context.
- 🌙 **Light/Dark Themes** – Switch between themes to reduce eye strain.
- 🧼 **Clean UI** – Aesthetic and distraction-free interface.
- 📤 **Real-Time Responses** – Thanks to Groq's lightning-fast inference API.

---

## 🛠️ Tech Stack

| Layer     | Technology                             |
|-----------|-----------------------------------------|
| Frontend  | HTML, CSS, JavaScript                   |
| Styling   | Custom CSS (Dark/Light Mode toggle)     |
| Backend   | FastAPI                                 |
| AI Engine | Groq API (LLaMA-4: `meta-llama/llama-4-scout-17b-16e-instruct`) |
| Deployment| Localhost / Cloud                       |

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.9+
- pip and virtualenv
- Groq API Key

---

### 🧠 Backend Setup (FastAPI + Groq API)

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CodeSensei.git
   cd CodeSensei

##Set up Python environment

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
