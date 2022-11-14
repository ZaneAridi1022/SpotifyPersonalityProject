import streamlit as st
import importlib.util

spec = importlib.util.spec_from_file_location(
    "SpotifyProject",
    'C:\\Users\\nikon\\SpotifyPersonalityProject\\SpotifyPersonalityPredictor\\ProjectSolution\\Prediction.py'
)
Predictor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Predictor)

# This page will be where our model displays it's prediction.

st.title("Unveiled: The Rhythm of your Soul")

makePrediction = st.button("Make Prediction!")

if makePrediction:
    prediction,test = Predictor.SpotifyModel(([st.session_state.parameters],""))
    st.subheader("Predictions: ")
    st.write("Extraversion: ",prediction[0][0])
    st.write('Agreeableness: ', prediction[0][1])
    st.write('Conscientiousness: ', prediction[0][2])
    st.write('Neuroticism: ', prediction[0][3])
    st.write('Openness: ', prediction[0][4])

    st.subheader("Self Evaluation: ")
    st.write('Extraversion: ', st.session_state.extraversion)
    st.write('Agreeableness: ', st.session_state.agreeableness)
    st.write('Conscientiousness: ', st.session_state.conscientiousness)
    st.write('Neuroticism: ', st.session_state.neuroticism)
    st.write('Openness: ', st.session_state.openness)


