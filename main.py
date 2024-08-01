import streamlit as st
import pandas

st.set_page_config(layout="wide")

ds = pandas.read_csv("data.csv")

st.header("The Best Company")
context1 = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
st.write(context1)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3,gap="medium")
with col1:
    for index, row in ds[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])

with col2:
    for index, row in ds[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])

with col3:
    for index, row in ds[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.image("images/" + row['image'])
        st.write(row['role'])