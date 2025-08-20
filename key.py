import streamlit as st
st.title("login")

username= st.text_input("enter user name")
email=st.text_input("enter your email")
password=st. text_input("enter your password")
if  st.button("login"):
     st. success("welldone")