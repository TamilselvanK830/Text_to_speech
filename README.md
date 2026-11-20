# 🎤 Text-to-Speech Application

## 📌 Project Overview

This is a Python-based Text-to-Speech application that converts written text into spoken audio using the `pyttsx3` library.

The application allows users to enter multiple sentences continuously and listens to each input until they type `exit`.

## ✨ Features

- Convert text into speech.
- Continuously accept multiple text inputs.
- Speak each sentence immediately.
- Keep running until the user types `exit`.
- Handle empty inputs.
- Works offline using the `pyttsx3` library.

## 🛠️ Technologies Used

- Python
- pyttsx3
- Git and GitHub
- VS Code

## 📂 Project Structure

```text
Text_to_speech_prt1/
│
├── demo.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/TamilselvanK830/Text_to_speech.git
```

### 2. Navigate to the project folder

```bash
cd Text_to_speech
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the following command:

```bash
python demo.py
```

### Example Output

```text
===== CONTINUOUS TEXT TO SPEECH =====
Type 'exit' to stop.

Enter text: Good morning
Enter text: Welcome to Python
Enter text: Have a nice day
Enter text: exit

Program stopped.
```

The application speaks each sentence entered by the user.

## 📚 Learning Outcomes

- Understanding Python loops.
- Working with user input.
- Using Python libraries.
- Implementing Text-to-Speech functionality.
- Handling empty input and exit conditions.
- Managing projects using Git and GitHub.

## 👨‍💻 Author

Tamilselvan

## 🔗 GitHub Repository

https://github.com/TamilselvanK830/Text_to_speech
