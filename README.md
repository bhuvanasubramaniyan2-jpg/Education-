# EduBuddy - Education Chatbot

A simple Flask-based education chatbot for a student project.

## Project Structure

```text
education_chatbot/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## How to Run

### 1. Open Command Prompt / PowerShell

Go to the project folder:

```powershell
cd education_chatbot
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate it

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If activation is blocked, you can still install the packages with:

```powershell
pip install -r requirements.txt
```

### 4. Install requirements

```powershell
pip install -r requirements.txt
```

### 5. Start the chatbot

```powershell
python app.py
```

### 6. Open in browser

Go to:

```text
http://127.0.0.1:5000
```

## Features

- Education-focused chatbot interface
- Flask backend
- Simple question-and-answer logic
- Responsive chat UI
- Easy to customize
- No paid API required
