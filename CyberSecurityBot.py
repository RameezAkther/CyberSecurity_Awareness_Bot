import streamlit as st
import google.generativeai as ggi
from PerformQuery import query_rag


fetcheed_api_key = "API_KEY_HERE"
ggi.configure(api_key = fetcheed_api_key)

model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message("GENERATE A JSON WITH THE QUESTION, CHOICES, CORRECT_ANSWER, AND EXPLANATION the question should be related to cybersecurity and also generate only one and don't repeat your previous question")
    return response

st.title("Cybersecurity Awareness Bot")

st.write("Hello there! I am a chatbot designed to educate you about cybersecurity and guide you on how to protect yourself from online threats. Whether you're a beginner or an experienced user, I’m here to provide you with valuable tips, insights, and best practices to ensure your online safety and security. Let's embark on this journey to make your digital life more secure!")

user_quest = st.text_input("Ask a question:")
btn = st.button("Ask")

if btn and user_quest:
    result = LLM_Response(user_quest)
    st.subheader("Response : ")
    st.text(result)