# Step 1: Install the tools we need
pip install openai streamlit # type: ignore

# Step 2: Write the code for Emily
import openai
import streamlit as st

# Step 3: Set up your API key
openai.api_key = "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"  # Replace this with your actual API key

# Step 4: Create Emily
st.title("Meet Emily! 🤖")
st.write("Emily is your friendly AI assistant. Ask her anything!")

# Step 5: Let Emily talk to you
user_input = st.text_input("You: ")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    emily_response = response['choices'][0]['message']['content']
    st.write(f"Emily: {emily_response}")