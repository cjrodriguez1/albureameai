import openai
import os
import json
import streamlit as st

from random import randrange
from google.cloud import storage





# pip install streamlit-chat
from streamlit_chat import message

openai.api_key = st.secrets["pass"]
#f = open("nuevas.csv", "a")

st.set_page_config(page_title="AlbureameAI", page_icon=":fire:")



mmap = {} #<--- map para leer los archivos csv
map_palab = {} #<--- map para las interpretaciones
map_cont = {} #<--- map para las contestaciones
map_comodines = {} #<--- map para los comodines
def get_map_palab(filename, value):
    file_palab = open(filename, "r", encoding='utf-8')
    for line in file_palab:
        all_words = line.split(",")
        for word in all_words:
            word = word.strip()
            if len(word) > 1:
                mmap[word.strip()] = value
    file_palab.close()

def populate_mmap(directory_name):
    directory = os.fsencode(directory_name)
    for file in os.listdir(directory):
        filename = os.fsencode(file).decode()
        value_word = filename.split(".")[0]
        get_map_palab(directory_name + "/" + filename, value_word)

populate_mmap("palabras")

def populate_given_map(directory_name, given_map):
    with open(directory_name, encoding='utf-8') as f:
        data = json.load(f)
    for key in data:
        given_map[key] = data[key]

populate_given_map("contestaciones/interpretaciones.json", map_palab)
populate_given_map("contestaciones/contextos.json", map_cont)
populate_given_map("contestaciones/comodines.json", map_comodines)


def generate_response(prompt):
    for word in prompt.split(" "):
        if mmap.get(word) != None:
            possib = map_palab.get(mmap.get(word))
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]
        elif map_palab.get(word) != None:
            possib = map_palab.get(word)
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]

    #f.write(prompt + "\n")
    comodines_list = map_comodines.get("comodines")
    index = randrange(len(comodines_list))
    return comodines_list[index] + "*"
    #return "No tengo contestación para '{}'".format(prompt)

#Creating the chatbot interface
st.title("Alburéame A.I.")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("Escribe abajo, novato:","", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

#f.close()