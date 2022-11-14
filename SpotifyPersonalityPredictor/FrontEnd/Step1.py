import streamlit as st

st.set_page_config(
    page_title="Rhythm of the Soul",
)

st.title("Finding Your Soul's Rhythm")

st.header("_What is this?_")

st.markdown("If you  give us your Spotify listening data...")

st.markdown("In return, we will give you...")

st.subheader("Your Personality!")

st.sidebar.success("Follow the steps to find your souls rhythm.")

st.header("_But how is this done?_")

st.markdown(
    "We process your spotify data by taking into account factors such as your listening time and features of your music taste such as danceability, energy, tempo, valence and more.."
)

st.markdown("After that, we let our AI model do the rest!")

st.subheader("By the end, we will have found your Soul's Rhythm!")