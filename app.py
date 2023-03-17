import streamlit as st

st.set_page_config(page_title="Albureame AI", page_icon=":wave:", layout="wide")

txtlist = ["Orale","que ","loco","valedor, te la bañaste"]

#HEADER SECTION
st.subheader("Hi, I am Chilango :wave:")
st.title("Una página de Albures")
st.write("I am passionate to write apps with Python and stuff")
st.write("[Learn More >](www.google.com)")
st.write("More stuff ovver here to see if i could deploy continously")
txt = st.text_area('Text to analyze', txtlist)
