import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=300)

with col2:
    st.title("Ryan O'Connor")
    content = """
    Hello, my name is Ryan O'Connor. I am recent first class honours graduate in Psychology from 
    South East Technological University, and a current postgraduate student in Data Science at the 
    Technological University of Dublin. I have built this website to showcase some of my projects that I have built 
    while learning Python. More projects will be added to it over time as my skills progress. 
    """
    st.info(content)

message = """
Below you can find some of my projects. Feel free to contact me !
"""
st.write(message)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://github.com/ryanoc21)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://github.com/ryanoc21)")

