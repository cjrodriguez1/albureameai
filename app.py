import streamlit as st
from streamlit_chat import message

st.set_page_config(page_title="Albureame AI", page_icon=":wave:", layout="wide")

txtlist = ["Orale","que ","loco","valedor, te la bañaste", "chido"]

#HEADER SECTION
st.subheader("Hi, I am Chilango :wave:")
st.title("Una página de Albures")
st.write("I am passionate to write apps with Python and stuff")
st.write("[Learn More >](www.google.com)")
st.write("More stuff ovver here to see if i could deploy continously")

message_history = []
bot_message_history = ["chid", "carnal", "valedor"]



# display all the previous message

#placeholder = st.empty()  # placeholder for latest message
'''
while(1):
    input_ = st.text_input("you:")
    message_history.append(input_)
    message(len(message_history))

    for message_ in message_history:
        message(message_)

    for message_ in bot_message_history:
        message(message_)
        
    with placeholder.container():
       message(message_history[-1]) # display the latest message
'''

# Create a text input and a text area in the Streamlit app
text_input = st.text_input("Enter some text:")
text_area = st.text_area("Text:")

st.write("Stuff", text_area)




