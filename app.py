# streamlit_app.py

import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the trained PyCaret model
model = load_model('4th_down_model')

st.set_page_config(page_title="4th Down Decision Assistant", layout="centered")
st.title("4th Down Decision Assistant")

st.markdown("Use this tool to see what the model recommends on 4th down based on game situation.")

# --- Input sliders ---
yardline = st.slider("Yardline (yards from end zone)", 1, 99, 50)
ydstogo = st.slider("Yards to Go for 1st Down", 1, 20, 5)
score_diff = st.slider("Score Differential (your team)", -30, 30, 0)
st.markdown("Time Remaining in Quarter")
minutes = st.slider("Minutes", 0, 15, 5)
seconds = st.slider("Seconds", 0, 59, 0)
quarter = st.slider("Quarter", 1, 4, 4)
own_timeouts = st.slider("Your Timeouts Remaining", 0, 3, 3)
opp_timeouts = st.slider("Opponent Timeouts Remaining", 0, 3, 3)


# --- Prediction ---
if st.button("Get Model Recommendation"):
    # Convert quarter time to full game time
    time_left = (4 - quarter) * 900 + (minutes * 60 + seconds)

    input_df = pd.DataFrame([{
        'yardline_100': yardline,
        'ydstogo': ydstogo,
        'score_differential': score_diff,
        'game_seconds_remaining': time_left,
        'qtr': quarter,
        'posteam_timeouts_remaining': own_timeouts,
        'defteam_timeouts_remaining': opp_timeouts
    }])

    result = predict_model(model, data=input_df)
    decision = result['prediction_label'][0]
    confidence = result['prediction_score'][0]

    st.markdown(f"### Model Recommends: **{decision.upper()}**")
    st.markdown(f"Confidence: **{confidence:.2%}**")
