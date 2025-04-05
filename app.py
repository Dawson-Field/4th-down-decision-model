# streamlit_app.py

import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# --- Page Configuration ---
st.set_page_config(page_title="4th Down Decision Assistant", layout="centered")

# --- Load Trained Model ---
model = load_model('4th_down_model')

# --- Title and Description ---
st.title("4th Down Decision Assistant")
st.markdown(
    """
    This tool was built to assist decision-making **from the offensive team’s point of view**.
    
    This application uses a machine learning model trained on NFL play-by-play data 
    to help teams make optimal decisions on 4th down: whether to go for it, punt, or attempt a field goal.
    """
)

st.markdown("---")

# --- Input Section: Game Situation ---
st.header("Game Situation")

yardline = st.slider("Yardline (yards from opponent's end zone)", min_value=1, max_value=99, value=50)
ydstogo = st.slider("Yards to Go for First Down", min_value=1, max_value=25, value=5)
score_diff = st.slider("Score Differential", min_value=-30, max_value=30, value=0)
quarter = st.slider("Quarter", min_value=1, max_value=4, value=4)

st.markdown("**Time Remaining in Quarter**")
col1, col2 = st.columns(2)
with col1:
    minutes = st.slider("Minutes", min_value=0, max_value=15, value=5)
with col2:
    seconds = st.slider("Seconds", min_value=0, max_value=59, value=0)


own_timeouts = st.slider("Your Team's Timeouts Remaining", min_value=0, max_value=3, value=3)
opp_timeouts = st.slider("Opponent's Timeouts Remaining", min_value=0, max_value=3, value=3)

st.markdown("---")

# --- Model Prediction ---
st.header("Model Recommendation")

if st.button("Get Recommendation"):
    # Convert quarter-based time into total game seconds remaining
    game_seconds_remaining = (4 - quarter) * 900 + (minutes * 60 + seconds)

    # Prepare input for prediction
    input_df = pd.DataFrame([{
        'yardline_100': yardline,
        'ydstogo': ydstogo,
        'score_differential': score_diff,
        'game_seconds_remaining': game_seconds_remaining,
        'qtr': quarter,
        'posteam_timeouts_remaining': own_timeouts,
        'defteam_timeouts_remaining': opp_timeouts
    }])

    # Generate prediction
    result = predict_model(model, data=input_df)
    decision = result['prediction_label'][0]
    confidence = result['prediction_score'][0]

    # Display result
    st.markdown(f"<h2 style='color:green;'>{decision.upper()}</h2>", unsafe_allow_html=True)
    st.markdown(f"**Model Confidence:** {confidence:.2%}")


    # Show input summary for transparency
    st.subheader("Input Summary")
    st.dataframe(input_df)

# --- Footer ---
st.markdown("---")
st.caption("Built by Dawson Field using PyCaret and NFL play-by-play data.")