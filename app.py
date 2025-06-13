import streamlit as st
import re
from prompts import build_tech_prompt
# from utils import get_openai_response

st.set_page_config(page_title="TalentScout Chatbot")

st.title("TalentScout - Hiring Bot")

# Initialize session state
if "stage" not in st.session_state:
    st.session_state.stage = "greet"
    st.session_state.candidate_info = {}
    st.session_state.tech_stack = ""

# Greet user
if st.session_state.stage == "greet":
    st.write("Hi! I'm Scout, your AI Hiring Assistant.")
    st.write("Let's begin your initial screening.")
    if st.button("Start"):
        st.session_state.stage = "name"

# Collect candidate info step-by-step
elif st.session_state.stage == "name":
    name = st.text_input("What's your full name?")
    if st.button("Next"):
        if name:
            st.session_state.candidate_info["name"] = name
            st.session_state.stage = "email"
        

elif st.session_state.stage == "email":
    email = st.text_input("Your email address?")
    if st.button("Next"):
        if not email:
            st.warning("Please enter your email.")
        elif not re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}$", email):
            st.error("Invalid email address. Example: abc@example.com")
        else:
            st.session_state.candidate_info["email"] = email
            st.session_state.stage = "phone"

elif st.session_state.stage == "phone":
    phone = st.text_input("Your phone number?")
    if st.button("Next"):
        if not phone:
            st.warning("Please enter your phone number.")
        elif not re.match(r"^\d{10}$", phone):
            st.error("Phone number must be exactly 10 digits.")
        else:
            st.session_state.candidate_info["phone"] = phone
            st.session_state.stage = "experience"

elif st.session_state.stage == "experience":
    exp = st.text_input("Years of experience?")
    if st.button("Next"):
        if exp:
            st.session_state.candidate_info["experience"] = exp
            st.session_state.stage = "position"

elif st.session_state.stage == "position":
    pos = st.text_input("Desired position(s)?")
    if st.button("Next"):
        if pos:
            st.session_state.candidate_info["position"] = pos
            st.session_state.stage = "location"

elif st.session_state.stage == "location":
    loc = st.text_input("Current location?")
    if st.button("Next"):
        if loc:
            st.session_state.candidate_info["location"] = loc
            st.session_state.stage = "tech_stack"

elif st.session_state.stage == "tech_stack":
    stack = st.text_input("List your tech stack (e.g., Python, Django, React):")
    if st.button("Next"):
        if stack:
            st.session_state.tech_stack = stack
            st.session_state.stage = "generate_questions"

    st.success("This concludes your screening. Our team will contact you if there's a match. Thank you!")
