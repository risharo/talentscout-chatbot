import streamlit as st

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
    st.session_state.stage = "name"

# Collect candidate info step-by-step
if st.session_state.stage == "name":
    name = st.text_input("What's your full name?")
    if name:
        st.session_state.candidate_info["name"] = name
        st.session_state.stage = "email"

elif st.session_state.stage == "email":
    email = st.text_input("Your email address?")
    if email:
        st.session_state.candidate_info["email"] = email
        st.session_state.stage = "phone"

elif st.session_state.stage == "phone":
    phone = st.text_input("Your phone number?")
    if phone:
        st.session_state.candidate_info["phone"] = phone
        st.session_state.stage = "experience"

elif st.session_state.stage == "experience":
    exp = st.text_input("Years of experience?")
    if exp:
        st.session_state.candidate_info["experience"] = exp
        st.session_state.stage = "position"

elif st.session_state.stage == "position":
    pos = st.text_input("Desired position(s)?")
    if pos:
        st.session_state.candidate_info["position"] = pos
        st.session_state.stage = "location"

elif st.session_state.stage == "location":
    loc = st.text_input("Current location?")
    if loc:
        st.session_state.candidate_info["location"] = loc
        st.session_state.stage = "tech_stack"

elif st.session_state.stage == "tech_stack":
    stack = st.text_input("List your tech stack (e.g., Python, Django, React):")
    if stack:
        st.session_state.tech_stack = stack
        st.session_state.stage = "generate_questions"

elif st.session_state.stage == "generate_questions":
    st.write("Thank you! Generating technical questions for you...")
    st.write("🧠 Coming soon: AI-generated questions based on your tech stack.")
    st.write("Stay tuned!")
