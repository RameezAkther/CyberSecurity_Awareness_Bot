import streamlit as st
from PerformQuery import query_rag      #load the function properly
import google.generativeai as ggi
import json
import random
import re

about = """**Cybersecurity Awareness Chatbot Overview**

The Cybersecurity Awareness Chatbot is an innovative application designed to educate users about protecting themselves from cyberattacks. Built using Streamlit, Google Generative AI, LangChain, ChromaDB, and Cohere embeddings, this chatbot leverages advanced technologies to provide interactive and informative content.

Key Features:
- **Retrieval-Augmented Generation (RAG)**: Utilizes RAG to retrieve relevant information from a PDF document based on user queries, ensuring accurate and contextually rich responses.
- **Quiz Session**: Offers a quiz session to engage users and test their knowledge of cybersecurity concepts, enhancing learning and retention.
- **Response Generation**: Generates responses using LangChain and Gemini AI, providing accurate and insightful information to users.

With its user-friendly interface and advanced features, the Cybersecurity Awareness Chatbot is a valuable tool for individuals looking to enhance their cybersecurity knowledge and protect themselves from online threats."""

api_key = "API_KEY_HERE" #replace you're API KEY here
ggi.configure(api_key = api_key)

flag = 1
used_questions = []

model = ggi.GenerativeModel("gemini-pro") 
chat = model.start_chat()

st.sidebar.title('Utilities')

with open('questions.json', 'r') as f:      #specify the path to the json file correctly
    questions = json.load(f)

selected_tab = st.sidebar.selectbox(
    "Select your preference:",
    ("Chat Session", "Quiz Session", "About")
)

def LLM_Response(question):
    try:
        response = chat.send_message(query_rag(question),stream=True)
        text_res = []
        for word in response:
            text_res.append(word.text)
        return " ".join(text_res)
    except:
        return "Error occured while handling the prompt this might be due to the fact that your prompt may contain explicit content please try someother promt 😓"

def get_random_question():
    global used_questions
    remaining_questions = [q for q in questions if q not in used_questions]

    if not remaining_questions:
        used_questions = []
        remaining_questions = questions

    random_question = random.choice(remaining_questions)
    used_questions.append(random_question)
    return random_question

def get_question():
    global flag
    if flag % 2 == 0 :
        try:
            response = chat.send_message("Generate a JSON with the question, choices, correct_answer, and explanation. The question should be related to cybersecurity and also generate only one and don't repeate the previous question.")
            temp = response.text
            match = re.search(r'\{.*\}', temp, re.DOTALL)
            
            data = json.loads(match.group(0))
            flag+=1
            return data
        except:
            return get_random_question()
    else:
        return get_random_question()

def initialize_session_state():
    session_state = st.session_state
    session_state.form_count = 0
    session_state.quiz_data = get_question()

def quizes():
    st.title('Cybersecurity Questions')
    
    if 'form_count' not in st.session_state:
        initialize_session_state()
    if not st.session_state.quiz_data:
        st.seesion_state.quiz_data=get_question()

    quiz_data = st.session_state.quiz_data
    
    st.markdown(f"Question: {quiz_data['question']}")
    
    form = st.form(key=f"quiz_form_{st.session_state.form_count}")
    user_choice = form.radio("Choose an answer:", quiz_data['choices'])
    submitted = form.form_submit_button("Submit your answer")
    
    if submitted:
        if user_choice == quiz_data['correct_answer']:
            st.success("Correct")
        else:
            st.error("Incorrect")
        st.markdown(f"Explanation: {quiz_data['explanation']}")
        
        another_question = st.button("Another question")
        with st.spinner("Calling the model for the next question"):
            session_state = st.session_state
            session_state.quiz_data= get_question()
        
        if another_question:
            st.session_state.form_count += 1
        else:
            st.stop()

def chat_session():
    st.title("CyberSecurity Awareness Bot")
    with st.chat_message(name="assistant"):
        st.write("Hello there! I am a chatbot designed to educate you about cybersecurity and guide you on how to protect yourself from online threats. Whether you're a beginner or an experienced user, I’m here to provide you with valuable tips, insights, and best practices to ensure your online safety and security. Let's embark on this journey to make your digital life more secure!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask something"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = LLM_Response(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if selected_tab == "Chat Session":
    chat_session()
elif selected_tab == "Quiz Session":
    quizes()
elif selected_tab == "About":
    st.title("About")
    st.markdown(about)