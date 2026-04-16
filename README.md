# 🐛 AI Code Debugger

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

**Upload a screenshot of your buggy code — AI finds the bug and fixes it.**

[🚀 Live Demo](https://code-debug-ger-ai.streamlit.app/) &nbsp;·&nbsp; [📁 GitHub](https://github.com/MZahidKamal/AI_Code_Debugger) &nbsp;·&nbsp; [💼 Portfolio](https://md-zahid-kamal.vercel.app/)

![App Preview](https://res.cloudinary.com/zahids-cloudinary/image/upload/v1776336510/ai_code_debugger_app_live_link_ss_xtpfxt.jpg)

</div>

---

## 🧠 What It Does

**AI Code Debugger** is a lightweight Streamlit web app powered by **Google Gemini**. Upload a screenshot of code that has an error — the AI analyzes it and returns either helpful hints or a full corrected solution, depending on what you need.

No copy-pasting. No terminal. Just a screenshot.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📸 **Screenshot Upload** | Supports `PNG`, `JPG`, `JPEG` code screenshots |
| 💡 **Hints Mode** | AI guides you toward the fix without giving it away — great for learning |
| ✅ **Solution Mode** | Full bug explanation + corrected code with markdown formatting |
| ⚡ **Instant Feedback** | Real-time spinner while AI processes your request |
| 🛡️ **Input Validation** | Clear error messages if image or mode is missing |
| 🔐 **Secure API Handling** | API key loaded from `.env` — never hardcoded |
| 📱 **Responsive UI** | Clean sidebar layout, works on any screen size |

---

## 🤖 AI Model

| | Detail |
|---|---|
| **Provider** | Google AI Studio |
| **Model** | Gemini 2.5 Flash (configurable via `.env`) |
| **Input** | Multimodal — image + text prompt |
| **Output** | Markdown-formatted bug explanation and/or corrected code |

The model is **not hardcoded** — you can swap it by changing `GEMINI_MODEL` in your `.env` file.

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **AI / LLM** | [Google Gemini API](https://ai.google.dev/) via `google-genai` SDK |
| **Image Processing** | [Pillow (PIL)](https://pillow.readthedocs.io/) |
| **Environment Config** | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| **Language** | Python 3.10+ |
| **Deployment** | [Streamlit Community Cloud](https://streamlit.io/cloud) |

---

## 📁 Project Structure

```
ai-code-debugger/
│
├── app.py                  # Main entry point — UI flow
├── ai_services.py          # Gemini API calls — debug_code()
├── ui_components.py        # Sidebar, validation — reusable UI
├── config.py               # Env loading + Gemini client init
│
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-code-debugger.git
cd ai-code-debugger
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env .env
```
Open `.env` and fill in your values:
```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash-preview-04-17
```
> Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Run the app
```bash
streamlit run main.py
```
The app will open at `http://localhost:8501`

---

## 🌐 Deployment (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. In **Advanced settings → Secrets**, add:
```
GEMINI_API_KEY = "your_key_here"
GEMINI_MODEL = "gemini-2.5-flash-preview-04-17"
```
4. Click **Deploy** — done ✅

---

## 👤 Author

<div align="center">

**Mohammad Zahid Kamal**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/md-zahid-kamal/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-F97316?style=for-the-badge&logo=firefox&logoColor=white)](https://md-zahid-kamal.vercel.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MZahidKamal)

</div>

---

<div align="center">
  <sub>Built with ❤️ using Streamlit & Google Gemini</sub>
</div>
