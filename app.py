import streamlit as st
from chatbot import chatbot_response

st.set_page_config(
    page_title="Customer Service Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Service Chatbot")

st.markdown(
    "Ask questions about orders, refunds, payments, accounts, and support."
)
st.info(
    "👋 Welcome! Ask me about orders, refunds, payments, accounts, or technical support."
)
dark_mode = st.sidebar.toggle(
    "🌙 Dark Mode"
)

if dark_mode:

    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
st.caption("🚀 Developed by Dushyant")
# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:

    st.title("About")

    st.write(
        "This chatbot is designed to assist customers with common inquiries related to orders, refunds, payments, accounts, and technical support. It uses machine learning to understand and respond to user queries."
    )

    st.markdown("---")

    st.markdown(
        "**👨‍💻 Developed by Dushyant**"
    )

    st.subheader("Technologies")

    st.write("""
    - Python
    - Streamlit
    - Scikit-Learn
    - TF-IDF
    - Logistic Regression
    """)

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# Chat input
user_input = st.chat_input(
    "Type your question..."
)

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.write(user_input)

    # Get chatbot response
    response = chatbot_response(user_input)

    with st.chat_message("assistant"):

        st.write(response)

    # Store bot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )