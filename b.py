import streamlit as st
import ollama

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Friendly AI Bot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 40px;
}

/* Title */
.title {
    text-align: center;
    color: #4f46e5;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
    margin-bottom: 30px;
}

/* Chat messages */
.user-message {
    background-color: #4f46e5;
    color: white;
    padding: 12px 18px;
    border-radius: 18px 18px 5px 18px;
    margin: 10px 0;
    margin-left: 20%;
    font-size: 16px;
}

.ai-message {
    background-color: white;
    color: #1e293b;
    padding: 12px 18px;
    border-radius: 18px 18px 18px 5px;
    margin: 10px 20% 10px 0;
    font-size: 16px;
    border: 1px solid #e2e8f0;
}

/* Input box */
.stTextInput > div > div > input {
    border: 2px solid #c7d2fe;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
}

/* Input focus */
.stTextInput > div > div > input:focus {
    border-color: #4f46e5;
}

/* Button */
.stButton > button {
    width: 100%;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    font-weight: 600;
}

/* Button hover */
.stButton > button:hover {
    background-color: #3730a3;
    color: white;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 30px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.markdown(
    '<div class="title">🤖 Friendly AI Bot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask me anything! I am here to help 😊</div>',
    unsafe_allow_html=True
)


# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f'<div class="user-message">👤 {message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="ai-message">🤖 {message["content"]}</div>',
            unsafe_allow_html=True
        )


# ---------------- INPUT ----------------

question = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)


# ---------------- ASK BUTTON ----------------

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question first 😊")

    else:

        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # Ask Ollama
        with st.spinner("🤔 Thinking..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        You are a friendly and funny AI assistant.

                        Explain things in simple language.

                        Be helpful, encouraging and friendly.

                        If the user is learning programming,
                        explain concepts step by step.
                        """
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

        answer = response["message"]["content"]

        # Add AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        # Refresh page
        st.rerun()


# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit + Ollama</div>',
    unsafe_allow_html=True
)

