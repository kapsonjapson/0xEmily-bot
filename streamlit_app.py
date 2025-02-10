from openai import OpenAI
import streamlit as st
import time

# Initialize the OpenAI client
client = OpenAI(api_key="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")  # Replace with your actual API key

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        color: #4F8BF9;
        background-color: #F0F2F6;
    }
    .stButton>button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #3a6bb0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and description
st.title("🤖 Emily - Your Advanced AI Assistant")
st.write("Welcome! Emily is here to help you with anything you need. Customize your experience below!")

# Sidebar for user preferences
with st.sidebar:
    st.header("Settings")
    user_name = st.text_input("Your Name", placeholder="Enter your name")
    chat_mode = st.selectbox(
        "Chat Mode",
        ["Friendly", "Professional", "Funny"],
        index=0,
        help="Choose how Emily should respond.",
    )
    st.write("---")
    st.write("**About Emily**")
    st.write("Emily is an AI assistant powered by OpenAI. She can help you with questions, advice, or just chat!")

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Function to generate Emily's response
def generate_response(user_input, chat_mode):
    try:
        # Add context based on chat mode
        if chat_mode == "Friendly":
            context = "You are a friendly and helpful AI assistant. Be warm and conversational."
        elif chat_mode == "Professional":
            context = "You are a professional AI assistant. Be concise and formal."
        elif chat_mode == "Funny":
            context = "You are a funny and witty AI assistant. Make jokes and keep the mood light."

        # Add user input to conversation history
        st.session_state.conversation.append({"role": "user", "content": user_input})

        # Generate response using OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                *st.session_state.conversation,
            ],
        )
        emily_response = response.choices[0].message.content

        # Add Emily's response to conversation history
        st.session_state.conversation.append({"role": "assistant", "content": emily_response})

        return emily_response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request. Please try again."

# Display conversation history
st.write("---")
st.subheader("Conversation")

for message in st.session_state.conversation:
    if message["role"] == "user":
        st.markdown(f"**You**: {message['content']}")
    else:
        st.markdown(f"**Emily**: {message['content']}")

# User input
user_input = st.text_input("Type your message here...", key="input")

# Send button
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        with st.spinner("Emily is thinking..."):
            response = generate_response(user_input, chat_mode)
            st.experimental_rerun()  # Refresh the app to show the new message

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.conversation = []
    st.experimental_rerun()

# Footer
st.write("---")
st.write("Thank you for chatting with Emily! Have a great day! 😊")