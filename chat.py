

import os
from openai import OpenAI
import streamlit as st

XAPI = "xai-ycwqLKangyJjUgFphVtmecTQcCfLad9BaV0tasNrCe1l6MdF44IkfnT1Q03r7xTqVib2pNPfvuNm7usi"
st.title("AI chatbot...")
st.subheader("by Dimitris Theodoropoulos")
#st.markdown("<h1 style='color: red;'>ΑΣΚΛΗΠΙΕΙΟ- chatGPT</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='color: blue;'>by Dimitris Theodoropoulos</h2>", unsafe_allow_html=True)

#st.image("me.jpg")

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []

def create_style_assistant(writing_example):
    XAI_API_KEY = XAPI
    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    # Define system message for simple responses
    system_message = "Answer with simple words only."
    return client, system_message

def generate_response(client, system_message, prompt):
    completion = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": system_message},
            *st.session_state.history,  # Include previous conversation history
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    my_writing_style = """YOUR WRITING EXAMPLES GO HERE"""

    # Create the assistant
    client, system_message = create_style_assistant(my_writing_style)
    st.session_state.client = client
    st.session_state.system_message = system_message

    NAME = st.text_input("Enter your name please if you want...:")
    prompt = st.text_input("Enter your question:")

    if NAME:
        if prompt:
            # Generate response and add it to the conversation history
            response = generate_response(client, system_message, prompt)
            st.session_state.history.append({"role": "user", "content": prompt})
            st.session_state.history.append({"role": "assistant", "content": response})

            # Display conversation history
            for message in st.session_state.history:
                if message["role"] == "user":
                    # st.write(f"**User:** {message['content']}")
                    st.write("**{}**:{}".format(NAME,message['content']))
                else:
                    st.write(f"**ΑΣΚΛΗΠΙΕΙΟ- chatGPT:** {message['content']}")

            # # Display conversation history
            # for message in st.session_state.history:
            #     if message["role"] == "user":
            #         st.write(f"**User:** {message['content']}")
            #     else:
            #         st.write(f"**Assistant:** {message['content']}")
    else: 
        if prompt:
            # Generate response and add it to the conversation history
            response = generate_response(client, system_message, prompt)
            st.session_state.history.append({"role": "user", "content": prompt})
            st.session_state.history.append({"role": "assistant", "content": response})

            # Display conversation history
            for message in st.session_state.history:
                if message["role"] == "user":
                    st.write(f"**User:** {message['content']}")
                    # st.write("{}:{}".format(NAME,message['content']))
                else:
                    st.write(f"**ΑΣΚΛΗΠΙΕΙΟ- chatGPT:** {message['content']}")  

