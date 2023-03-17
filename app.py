import streamlit as st

st.set_page_config(page_title="Albureame AI", page_icon=":wave:", layout="wide")

#HEADER SECTION
st.subheader("Hi, I am Chilango :wave:")
st.title("Una página de Albures")
st.write("I am passionate to write apps with Python and stuff")
st.write("[Learn More >](www.google.com)")
st.write("More stuff ovver here to see if i could deploy continously")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
