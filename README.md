
# 💡 CodeSensei

**CodeSensei** is an AI-powered coding assistant that helps you write, understand, and explore code using natural language. Whether you're debugging, learning a new language, or need help generating code, CodeSensei is your go-to companion.

---

## 🚀 Features

- 🔍 **Explain Mode** – Understand complex code in simple terms.
- ⚡ **Generate Mode** – Instantly generate code snippets or algorithms.
- 💬 **Ask Mode** – Ask questions about programming concepts or syntax.
- 🧠 **Auto Mode** – Context-aware suggestions as you type.
- 🌙 **Light/Dark Themes** – Easily toggle between day and night modes.
- 🧼 **Clean UI** – Minimal, focused interface for seamless productivity.

---

## 🛠️ Tech Stack

| Layer        | Tech                        |
|--------------|-----------------------------|
| Frontend     | HTML, CSS, JavaScript       |
| Styling      | Pure CSS                    |
| Backend      | FastAPI                     |
| AI Engine    | Meta LLaMA-4-Scout-17B      |
| Deployment   | Localhost / Custom Hosting  |

---

## 🧑‍💻 Getting Started

### Prerequisites

- Python (v3.9+)
- `pip`, `virtualenv`
- Access to Groq API (Meta LLaMA model)

## 🔧 Frontend Setup (Pure HTML/CSS/JS)

```bash
# Clone the repo
git clone https://github.com/your-username/CodeSensei.git
cd CodeSensei
```

## 🧠 Backend Setup (FastAPI + Groq API)

### Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run FastAPI server
```bash
uvicorn app.main:app --reload
```

---

## ⚠️ Make sure the Groq API key is added in your `.env` file and the model used is supported (e.g., `meta-llama/llama-4-scout-17b-16e-instruct`).

---

## 📁 Project Structure
```bash
CodeSensei/
│
├── app/
│   ├── main.py
│   └── groq_api.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── .env
├── README.md
└── requirements.txt
```
---
## ✨ Screenshots
- Light Mode  
![Light Mode](https://github.com/user-attachments/assets/0b5783a9-bca7-4f20-84e4-74e30ca7df89)

- Dark Mode  
![Dark Mode](https://github.com/user-attachments/assets/fc240cf5-bad1-44b4-8383-8cef60482d57)

---

## 📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

## 🙌 Acknowledgements
- Meta’s LLaMA
- FastAPI
- Groq API
- HTML/CSS/JS

---


