# 4th Down Decision Assistant

This project uses a machine learning model trained on historical NFL play-by-play data to help NFL teams decide whether to go for it, punt, or kick a field goal on 4th down.

## Goal

To support **data-driven decision-making** in football by modeling optimal 4th down decisions based on historical outcomes and real-game scenarios.

---

## Try the App

**Use the interactive tool here:**  
[https://dawsonfield-4th-down-decision-model.hf.space](https://dawsonfield-4th-down-decision-model.hf.space)

You can input any 4th down scenario and the model will recommend the best action.

---

## What the Model Considers

- Field position (yards from opponent's end zone)
- Yards to go for a first down
- Score differential
- Quarter
- Time remaining in the quarter
- Timeouts remaining for both teams

---

## How It Works

- Built using `nfl_data_py`, `pandas`, and `PyCaret`
- Trained on past seasons and tested on 2024 data
- Predicts the optimal 4th down decision based on:
  - Field position
  - Yards to go
  - Score differential
  - Time remaining
  - Quarter
  - Timeouts


## Files Included

- `streamlit_app.py`: Streamlit app for real-time predictions
- `fourthdownmodel.ipynb`: Notebook with full data prep, model training, and visualizations
- `requirements.txt`: Project dependencies

## Built With

- [PyCaret](https://pycaret.org/) for low-code model training
- [nfl_data_py](https://github.com/nflverse/nfl_data_py) for play-by-play NFL data
- [Streamlit](https://streamlit.io/) for deployment
- [Hugging Face Spaces](https://huggingface.co/spaces) for free hosting

## Author

Built by **Dawson Field**  
[LinkedIn](https://www.linkedin.com/in/dawson-field)
