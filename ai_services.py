"""
ai_services.py
--------------
Gemini API-এর সাথে সব যোগাযোগ এই ফাইলে।
main.py এখান থেকে শুধু debug_code() function-টি import করে।
"""

from PIL import Image
from config import client, GEMINI_MODEL


def debug_code(image: Image.Image, mode: str) -> str:
    """
    একটি code screenshot এবং mode নিয়ে Gemini-কে পাঠায়।
    Gemini হয় Hint দেবে, নয়তো সম্পূর্ণ Solution দেবে।

    Parameters:
        image (Image.Image) : user-এর upload করা PIL Image
        mode (str)          : "Hints" অথবা "Solution with code"

    Returns:
        str: Gemini-এর markdown-formatted response
    """

    # mode অনুযায়ী আলাদা prompt তৈরি করো
    if mode == "Hints":
        prompt = (
            "You are an expert code debugger. "
            "The image contains code with one or more bugs. "
            "Do NOT give the solution or corrected code. "
            "Instead, provide clear hints that guide the developer "
            "to find and fix the bug themselves. "
            "Use markdown formatting with proper headings and bullet points."
        )
    else:  # "Solution with code"
        prompt = (
            "You are an expert code debugger. "
            "The image contains code with one or more bugs. "
            "Explain what the bug or error is, why it happens, "
            "and then provide the fully corrected code. "
            "Use markdown formatting with proper headings and code blocks."
        )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[image, prompt],
    )

    return response.text
