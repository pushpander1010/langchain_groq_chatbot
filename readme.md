# 🧠 ChatBot

A multi-persona AI chatbot built using **LangChain**, **Groq LLMs**, and **Streamlit**, with conversation history scoped per topic and expert. Deployed on **Streamlit Cloud**.

🌐 **Live Demo**: [pushpander-chatbot.streamlit.app](https://pushpander-chatbot.streamlit.app)

---

## 🚀 Features

- ✅ Choose from different expert personas like Doctor, Lawyer, Toddler, etc.
- ✅ Talk about multiple topics (Academics, Fun, Romance, Wars, etc.)
- ✅ Chat history is maintained **separately per expert-topic combo**
- ✅ Fast and smart responses powered by **Meta LLaMA 4 Scout model via Groq API**
- ✅ Lightweight and interactive frontend using **Streamlit**

---

## 🧰 Tech Stack

| Component           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **[Streamlit](https://streamlit.io/)**       | Frontend UI and web app deployment                                             |
| **[LangChain](https://www.langchain.com/)** | Prompt management, memory handling, and LLM abstraction                        |
| **[Groq API](https://groq.com/)**            | LLM backend (meta-llama/llama-4-scout-17b-16e-instruct) for ultra-fast inference |
| **Python**           | Core programming language                                                   |
| **.env** + `dotenv`  | Secure environment variable management                                      |

---

## 📁 Project Structure

simple_chatbot/
├── main.py # Main Streamlit app logic
├── requirements.txt # Python dependencies
├── .env # API key (not committed to Git)
├── .gitignore