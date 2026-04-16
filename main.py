"""
main.py
------
Streamlit app-এর main entry point।
এই ফাইলটি শুধু UI flow সামলায়।

AI logic      → ai_services.py
UI components → ui_components.py
Config        → config.py
"""


import streamlit as st
from ai_services import debug_code
from ui_components import render_sidebar, validate_inputs


# ---- Page Config ----
# Browser tab-এর title এবং icon set করা হচ্ছে
st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🐛",
    layout="wide",
)


# ---- Header ----
st.title("🐛 AI Code Debugger")
st.markdown(
    "তোমার code-এর screenshot upload করো। "
    "AI bug খুঁজে বের করে hint অথবা সম্পূর্ণ solution দেবে।"
)
st.divider()


# ---- Sidebar থেকে সব input নাও ----
uploaded_file, pil_image, mode, pressed = render_sidebar()


# ---- Debug Button চাপার আগে কিছুই দেখাবে না ----
if pressed:

    # Input validation — কোনো সমস্যা থাকলে নিচের কোড চলবে না
    if not validate_inputs(uploaded_file, mode):
        st.stop()

    # ---- Result Section ----
    with st.container(border=True):

        # mode অনুযায়ী section title বদলাও
        if mode == "Hints":
            st.subheader("💡 Hints")
        else:
            st.subheader("✅ Solution with Code")

        # API call চলার সময় spinner দেখাও
        with st.spinner("AI তোমার code বিশ্লেষণ করছে..."):
            result = debug_code(pil_image, mode)

        # Gemini-এর markdown response সরাসরি render করো
        st.markdown(result)
