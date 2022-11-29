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
    st.write('Extraversion is a personality trait characterized by excitability, sociability, talkativeness, assertiveness, and high amounts of emotional expressiveness. The trait is marked by pronounced engagement with the external world. Extraverts enjoy interacting with people, and are often perceived as full of energy. They tend to be enthusiastic, action-oriented individuals. They possess high group visibility, like to talk, and assert themselves. Extraverted people may appear more dominant in social settings, as opposed to introverted people in this setting.')
    st.write('Agreeableness: ', st.session_state.agreeableness)
    st.write('The agreeableness trait reflects individual differences in general concern for social harmony. Agreeable individuals value getting along with others. They are generally considerate, kind, generous, trusting and trustworthy, helpful, and willing to compromise their interests with others.')
    st.write('Conscientiousness: ', st.session_state.conscientiousness)
    st.write('Conscientiousness is a tendency to display self-discipline, act dutifully, and strive for achievement against measures or outside expectations. It is related to the way in which people control, regulate, and direct their impulses. High conscientiousness is often perceived as being stubborn and focused. Low conscientiousness is associated with flexibility and spontaneity, but can also appear as sloppiness and lack of reliability. High scores on conscientiousness indicate a preference for planned rather than spontaneous behavior.')
    st.write('Neuroticism: ', st.session_state.neuroticism)
    st.write('Those who score high in neuroticism are emotionally reactive and vulnerable to stress. They are more likely to interpret ordinary situations as threatening. They can perceive minor frustrations as hopelessly difficult. They also tend to be flippant in the way they express emotions. Their negative emotional reactions tend to persist for unusually long periods of time, which means they are often in a bad mood. For instance, neuroticism is connected to a pessimistic approach toward work, to certainty that work impedes personal relationships, and to higher levels of anxiety from the pressures at work.')
    st.write('Openness: ', st.session_state.openness)
    st.write('Openness to experience is a general appreciation for art, emotion, adventure, unusual ideas, imagination, curiosity, and variety of experience. People who are open to experience are intellectually curious, open to emotion, sensitive to beauty and willing to try new things. They tend to be, when compared to closed people, more creative and more aware of their feelings. They are also more likely to hold unconventional beliefs. High openness can be perceived as unpredictability or lack of focus, and more likely to engage in risky behavior or drug-taking.')


