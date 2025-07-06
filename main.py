from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,AIMessagePromptTemplate,HumanMessagePromptTemplate,SystemMessagePromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Streamlit app
st.set_page_config(page_title="ChatBot", page_icon="💬")
st.title("ChatBot")

def onSelect():
    st.session_state.chat_history=[]


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

model=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",temperature=0.7)
expert=st.selectbox("Select an expert",["Doctor","Cricketer","Footballer","Toddler","Professor","Lawyer","Liar","Fool","God"],on_change=onSelect)
topic=st.selectbox("Select an Topc",["Acedemics","Fun","Romance","wars","General Knowledge","Sports","Spiritual"],on_change=onSelect)
inp=st.chat_input("Enter your question here.")
prompt=ChatPromptTemplate([("system","You are the best {expert} and you give brief messages to queries"),
                           MessagesPlaceholder(variable_name="chat_history"),
                                  ("human","topic is {topic},talk about {inp}")])
mod=prompt|model

# Old messages gets printed

for msgs in st.session_state.chat_history:
    if "human" in msgs:
        with st.chat_message("user"):
            st.write(msgs[1])
    else:
        with st.chat_message("ai"):
            st.write(msgs[1])


if inp:
    with st.chat_message("user"):
        st.session_state.chat_history.append(("human",inp))
        st.write(str(inp))
    with st.chat_message("ai"):
        result=mod.invoke({"expert":expert,"topic":topic,"inp":inp,"chat_history":st.session_state.chat_history})
        st.session_state.chat_history.append(("ai",result.content))
        st.write(result.content)
