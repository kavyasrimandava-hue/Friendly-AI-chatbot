import streamlit as st
st.title("Job Application")
st.header("Registration")
name=st.text_input("enter your name:")
message=st.text_input("Enter your message:")
age=st.text_input("Enter your age:")
date=st.date_input("Select a date:")
time=st.time_input("Select a time:")
st.success("operation done successfully")


