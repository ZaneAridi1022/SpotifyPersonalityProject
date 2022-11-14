import streamlit as st
from PIL import Image
import os

# This page is to explain how a user can download their spotify data and upload it to our website for analysis

st.title("What's The Rhythm of Your Soul?")

st.header("In order for us to find your souls rhythm we need to know you better.")

st.subheader("On this page you will find every step you need to download your spotify data and upload it to our webiste so we can find your soul's rhythm!")

option = st.selectbox("Select Accessing Your Data To Get Started!", ("", "Accessing Your Data"))

# print()
# #change paths for these, I'm not sure what to make them

image_step_1 = Image.open("../../../../../Users/nikon/SpotifyPersonalityProject/SpotifyPersonalityPredictor/FrontEnd/pages/Images/Step_Image_1.png")

image_step_2 = Image.open(
    "../../../../../Users/nikon/SpotifyPersonalityProject/SpotifyPersonalityPredictor/FrontEnd/pages/Images/Step_Image_2.png"
)

image_step_3 = Image.open(
    "../../../../../Users/nikon/SpotifyPersonalityProject/SpotifyPersonalityPredictor/FrontEnd/pages/Images/Step_Image_3.png"
)

if option == (""):
    st.subheader("Click the drop-down menu and select Accessing Your Data!")
elif (option == "Accessing Your Data"):
    st.header("How to collect and access your data!")
    st.subheader("Step 1: Log Into Spotify and Find Account Page")
    st.image(image_step_1)
    st.subheader("Step 2: Navigate To The Privacy Settings Section On The Left Side Menu")
    st.image(image_step_2)
    st.subheader("Step 3: Scroll To The Bottom, Click The 'Request Your Data' Button, And Verify Request In Your Email!")
    st.image(
        image_step_3,
        caption=
        "Note that this process may take up to One Week before it is in your email!"
    )


st.file_uploader("Please upload your Spotify data here",
                 accept_multiple_files=True)
