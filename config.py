"""
config.py
---------
Environment variable লোড করা হয় এবং
Gemini API client একবার initialize করা হয়।
বাকি সব ফাইল এখান থেকে client ও model নাম import করে নেয়।
"""


import os
from google import genai
from dotenv import load_dotenv


# .env ফাইল থেকে সব variable লোড করো
load_dotenv()

_api_key = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")


# API key না পেলে শুরুতেই পরিষ্কার error দাও
if not _api_key:
    raise EnvironmentError(
        "GEMINI_API_KEY পাওয়া যায়নি। "
        ".env ফাইলে GEMINI_API_KEY=your_key_here লিখে রাখো।"
    )


if not GEMINI_MODEL:
    raise EnvironmentError(
        "GEMINI_MODEL পাওয়া যায়নি। "
        ".env ফাইলে GEMINI_MODEL=model_name লিখে রাখো।"
    )


# পুরো app জুড়ে এই একটি client instance ব্যবহার হবে
client = genai.Client(api_key=_api_key)
