import openai
import os
import json
import re
import streamlit as st

from random import randrange

# pip install streamlit-chat
from streamlit_chat import message

openai.api_key = st.secrets["pass"]
#f = open("nuevas.csv", "a")

st.set_page_config(page_title="AlbureameAI", page_icon=":fire:")

#Creating the chatbot interface
st.title(":fire: Alburéame A.I.:fire:")


# Maps required
mmap = {} #<--- map para leer los archivos csv
map_palab = {} #<--- map para las interpretaciones
map_cont = {} #<--- map para las contestaciones
map_comodines = {} #<--- map para los comodines

# These next two methods together generate map off the CSV files
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



# Generating maps off the JSON files
def populate_given_map(directory_name, given_map):
    with open(directory_name, encoding='utf-8') as f:
        data = json.load(f)
    for key in data:
        given_map[key] = data[key]

# Call to method that generates maps off CSV files
populate_mmap("palabras")

# Call to method that generates maps off the JSON files
populate_given_map("contextos/interpretaciones.json", map_palab)
populate_given_map("contextos/contestaciones.json", map_cont)
populate_given_map("contextos/comodines.json", map_comodines)

def detectar_calambur(prompt):
    alltext = re.sub('[^A-Za-z0-9]+', '', prompt)
    for key in mmap.keys():
        if key in alltext:
            possib = map_palab.get(mmap.get(key))
            index = randrange(len(possib))
            responses = map_cont[possib[index]]
            index = randrange(len(responses))
            return responses[index]
    return None

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

    calambur_resp = detectar_calambur(prompt)
    if calambur_resp != None:
        return calambur_resp

    #f.write(prompt + "\n")
    comodines_list = map_comodines.get("comodines")
    index = randrange(len(comodines_list))
    return comodines_list[index]
    #return "No tengo contestación para '{}'".format(prompt)



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