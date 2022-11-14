import streamlit as st

# This page will ask the user if we have their consent to use their data to help train our model

st.title("Tuning the Flow")

st.header("Your privacy is important to us, if you click the button below you are consenting to letting us save your data to help better train our model for future use!")

buttonClicked = st.button("Accept Terms")

if buttonClicked:
    st.write("Consent granted!")
