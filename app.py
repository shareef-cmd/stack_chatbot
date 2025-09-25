import streamlit as st
import random

# Define responses
responses = {
    "greeting": ["Hello! 👋 Welcome to Stack AI Centre. How can I help you?",
                 "Hi there! Ask me anything about our courses and admissions."],
    "courses": ["We offer Data Science, AI, ML, and Full Stack Development courses."],
    "fees": ["Data Science is ₹40,000, AI/ML is ₹50,000."],
    "admission": ["To apply, fill out our admission form and attend a short interview."],
    "placement": ["Yes! 🎓 We provide placement assistance with top companies."],
    "goodbye": ["Goodbye! 👋 Thanks for visiting."],
    "fallback": ["Sorry, I didn’t understand that 🤔. Can you rephrase?"]
}

# Intent detection
def get_intent(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif "course" in user_input:
        return "courses"
    elif "fee" in user_input or "cost" in user_input or "price" in user_input:
        return "fees"
    elif "admission" in user_input or "apply" in user_input or "join" in user_input:
        return "admission"
    elif "placement" in user_input or "job" in user_input or "company" in user_input:
        return "placement"
    elif any(word in user_input for word in ["bye", "thanks", "exit", "quit"]):
        return "goodbye"
    else:
        return "fallback"

# --- Streamlit UI ---
st.title("🤖 Stack AI Centre Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You: ", "")

if user_input:
    intent = get_intent(user_input)
    response = random.choice(responses[intent])
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

# Display chat history
for role, msg in st.session_state.chat:
    st.markdown(f"**{role}:** {msg}")
