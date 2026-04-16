"""
ui_components.py
----------------
Streamlit UI-এর reusable অংশগুলো এখানে।
main.py এখান থেকে import করে ব্যবহার করে।
"""


import streamlit as st
from PIL import Image


def render_sidebar() -> tuple:
    """
    Sidebar render করে এবং user-এর সব input ফেরত দেয়।

    Returns:
        tuple:
            - uploaded_file : Streamlit UploadedFile object অথবা None
            - pil_image     : PIL Image object অথবা None
            - mode          : "Hints" অথবা "Solution with code" অথবা None
            - pressed       : Debug button চাপা হয়েছে কি না (bool)
    """

    with st.sidebar:
        st.header("⚙️ Controls")

        # ---- Image Uploader ----
        uploaded_file = st.file_uploader(
            "Upload your code screenshot",
            type=["png", "jpg", "jpeg"],
        )

        # uploaded file থাকলে PIL Image-এ রূপান্তর করো
        pil_image = None
        if uploaded_file:
            pil_image = Image.open(uploaded_file)
            # Sidebar-এ ছবির একটি ছোট preview দেখাও
            st.image(uploaded_file, caption="Uploaded Screenshot", use_container_width=True)

        st.divider()

        # ---- Mode Selector ----
        # radio button দিয়ে দুটো option দেখাও
        mode = st.radio(
            "What do you need?",
            options=["Hints", "Solution with code"],
            index=None,  # শুরুতে কিছুই selected থাকবে না
        )

        st.divider()

        # ---- Debug Button ----
        pressed = st.button(
            "🐛 Debug Code",
            type="primary",
            use_container_width=True,
        )

    return uploaded_file, pil_image, mode, pressed


def validate_inputs(uploaded_file, mode: str | None) -> bool:
    """
    User input সঠিক আছে কি না যাচাই করে।
    কোনো সমস্যা থাকলে st.error() দিয়ে warning দেখায় এবং False ফেরত দেয়।

    Parameters:
        uploaded_file : Streamlit UploadedFile অথবা None
        mode          : selected mode অথবা None

    Returns:
        bool: সব input ঠিক থাকলে True, নইলে False
    """

    valid = True

    if not uploaded_file:
        st.error("⚠️ একটি code screenshot upload করতে হবে।")
        valid = False

    if not mode:
        st.error("⚠️ 'Hints' অথবা 'Solution with code' — একটি option বেছে নিতে হবে।")
        valid = False

    return valid
