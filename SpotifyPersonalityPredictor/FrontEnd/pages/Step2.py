import streamlit as st

# This page is to explain how a user can download their spotify data and upload it to our website for analysis

st.title("What's The Rhythm of Your Soul?")

st.header("In order for us to find your souls rhythm we need to know you better.")

st.subheader("On this page you will find every step you need to download your spotify data and upload it to our webiste so we can find your soul's rhythm!")

st.file_uploader("Please upload your Spotify data here",
                 accept_multiple_files=True)
