from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="ChatBot", page_icon="💬")
st.title("ChatBot")

# Initialize main history dict if not exists
if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

# Called when selectbox changes
def onSelect():
    expert = st.session_state.selected_expert
    topic = st.session_state.selected_topic
    key = f"{topic}_{expert}"
    if key not in st.session_state.chat_history:
        st.session_state.chat_history[key] = []

# Selections with keys
expert = st.selectbox("Select an expert", ["Doctor", "Cricketer", "Footballer", "Toddler", "Professor", "Lawyer", "Liar", "Fool", "God"], key="selected_expert", on_change=onSelect)
topic = st.selectbox("Select a Topic", ["Academics", "Fun", "Romance", "Wars", "General Knowledge", "Sports", "Spiritual"], key="selected_topic", on_change=onSelect)

# Get current session key
session_key = f"{topic}_{expert}"
if session_key not in st.session_state.chat_history:
    st.session_state.chat_history[session_key] = []

# LangChain setup
model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.7)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the best {expert} and you give brief messages to queries."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "topic is {topic}, talk about {inp}")
])
chain = prompt | model

# Display past messages
for msg in st.session_state.chat_history[session_key]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("ai"):
            st.write(msg.content)

# Input handling
inp = st.chat_input("Enter your question here.")
if inp:
    # Append human message
    st.session_state.chat_history[session_key].append(HumanMessage(content=inp))
    with st.chat_message("user"):
        st.write(inp)

    # Generate and append AI message
    result = chain.invoke({
        "expert": expert,
        "topic": topic,
        "inp": inp,
        "chat_history": st.session_state.chat_history[session_key]
    })
    st.session_state.chat_history[session_key].append(AIMessage(content=result.content))
    with st.chat_message("ai"):
        st.write(result.content)
