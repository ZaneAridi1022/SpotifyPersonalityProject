import streamlit as st

# This page will only be available if they consent to helping us train the AI. This page will have a bunch of text inputs that are our questions from the personality questionare, this page will display their calculated Nig 5 from answering the questionare questions and we will use their inputs to add to our dataset.

st.title("Predict your Rythm")

st.write("Thank you for your participation!")

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

extraversion = (6-ques1) + ques6

agreeableness = (6-ques7) + ques2

conscientiousness = (6-ques3) + ques8

neuroticism = (6-ques4) + ques9

openness = (6-ques5) + ques10