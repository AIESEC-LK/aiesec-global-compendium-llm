import streamlit as st
from streamlit_chat import message
from utils import create_retrieval
import os

# Load OpenAI API key from Streamlit secrets
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Headlines
st.title("Chat with the Global Compendium \(β Version)")
st.subheader("Product of AIESEC in Sri Lanka")

st.write("<br>", unsafe_allow_html=True)

# Sessions
if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Ayobowan! Welcome to AIESEC in Sri Lanka's Chat with Global Compendium App.\nHow can I assist you?"]

if 'requests' not in st.session_state:
    st.session_state['requests'] = []

# Container for chat history
response_container = st.container()

# Container for text box
textcontainer = st.container()

with textcontainer:
    query = st.chat_input("Enter Your Question..", key="input")

    if query:
        with st.spinner("typing..."):
            try:
                chain = create_retrieval()
                response = chain.invoke({"input": query})
                response = response["answer"]
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.stop()
        st.session_state.requests.append(query)
        st.session_state.responses.append(response)
        st.session_state["query"] = ""

with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i], key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')


st.write("<br><br><br>", unsafe_allow_html=True)

#Footer
st.write("<p style='text-align: center;'>Please note that this is a beta app and we are working on more the finetuning and the user interface as well. If you have any suggestion or feedback please contact fouzul.hassan@aiesec.net</p>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

#Footer
st.write("<p style='text-align: center;'>Made with ❤️ by &lt;/Dev.Team&gt; of AIESEC in Sri Lanka</p>", unsafe_allow_html=True)
