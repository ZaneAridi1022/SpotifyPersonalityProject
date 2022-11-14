import streamlit as st

# This page will only be available if they consent to helping us train the AI. This page will have a bunch of text inputs that are our questions from the personality questionare, this page will display their calculated Nig 5 from answering the questionare questions and we will use their inputs to add to our dataset.

st.title("Predict your Rythm")

st.subheader(
    "Answering these questions will give us your personality as you see it. We will train our model to try and guess the outcomes using this data. When our model does its prediction, its without having seen your data at all. When moving to step 5 make sure to keep in mind what your personality scores are from this page so you can check to see if our prediction is close to your actual outcomes! Thank you for your participation!"
)

st.write("_1 -> Strongly Disagree, 5 -> Strongly Agree_")
ques1 = st.radio("I see myself as someone who is reserved",(1, 2, 3, 4, 5))

ques2 = st.radio("I see myself as someone who is generally trusting",(1, 2, 3, 4, 5))

ques3 = st.radio("I see myself as someone who tends to be lazy",(1, 2, 3, 4, 5))

ques4 = st.radio("I see myself as someone who is relaxed, handles stress well",(1, 2, 3, 4, 5))

ques5 = st.radio("I see myself as someone who has few artistic interests",(1, 2, 3, 4, 5))

ques6 = st.radio("I see myself as someone who is outgoing, sociable",(1, 2, 3, 4, 5))

ques7 = st.radio("I see myself as someone who tends to find fault with others",(1, 2, 3, 4, 5))

ques8 = st.radio("I see myself as someone who does a thorough job",(1, 2, 3, 4, 5))

ques9 = st.radio("I see myself as someone who gets nervous easily",(1, 2, 3, 4, 5))

ques10 = st.radio("I see myself as someone who has an active imagination",(1, 2, 3, 4, 5))

st.session_state.extraversion = (6-ques1) + ques6

st.session_state.agreeableness = (6-ques7) + ques2

st.session_state.conscientiousness = (6-ques3) + ques8

st.session_state.neuroticism = (6-ques4) + ques9

st.session_state.openness = (6-ques5) + ques10

st.write('Extraversion: ', st.session_state.extraversion)
st.write('Agreeableness: ', st.session_state.agreeableness)
st.write('Conscientiousness: ', st.session_state.conscientiousness)
st.write('Neuroticism: ', st.session_state.neuroticism)
st.write('Openness: ', st.session_state.openness)
