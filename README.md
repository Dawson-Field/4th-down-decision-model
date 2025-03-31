# 4th Down Decision Assistant

This project uses a machine learning model trained on historical NFL play-by-play data to help teams decide whether to **go for it**, **punt**, or **kick a field goal** on 4th down.

Built as a football strategy tool, it brings advanced analytics into one of the most critical in-game decisions — with real-time recommendations based on game context.

---

## Project Goal

To support **data-driven decision-making** in football by modeling optimal 4th down choices based on historical outcomes and in-game variables.

---

## Try the App

👉 [**Launch the 4th Down Decision Assistant**](https://dawsonfield-4th-down-decision-model.hf.space)  

> Input any 4th down scenario and receive a model-generated recommendation in real-time.

---

## Model Overview

The model was trained using:
- `nfl_data_py` play-by-play data (multiple NFL seasons)
- `PyCaret` for model training and evaluation

### Features Considered:
- Field position (yards from opponent's end zone)
- Yards to go for a first down
- Score differential
- Quarter
- Time remaining in the quarter
- Timeouts remaining (offense & defense)

### Outcome:
The model classifies each scenario into one of three decisions:
- Go for it
- Punt
- Field Goal Attempt

---

## Development & Testing

- Built-in Python with full preprocessing, feature engineering, and model training in `fourthdownmodel.ipynb`
- Tested on unseen 2024 play-by-play data to validate predictive performance
- Future enhancements may include:
  - Win probability integration
  - EPA (Expected Points Added) impact analysis

---

## Repo Structure

| File | Description |
|------|-------------|
| `app.py` | Streamlit app for real-time predictions |
| `fourthdownmodel.ipynb` | Full notebook for data prep, model training, and evaluation |
| `requirements.txt` | Python dependencies |
| `4th_down_model.pkl` | Trained PyCaret classification model |

---

## Built With

- [PyCaret](https://pycaret.org/) – Automated machine learning
- [nfl_data_py](https://github.com/nflverse/nfl_data_py) – NFL play-by-play data
- [Streamlit](https://streamlit.io/) – Frontend interface
- [Hugging Face Spaces](https://huggingface.co/spaces) – App hosting

---

## Author

Built by **Dawson Field**  
[LinkedIn](https://www.linkedin.com/in/dawson-field)  

---

## Summary

This project combines football strategy with predictive modeling to guide 4th down decision-making. By analyzing past outcomes and in-game situations, it offers coaches, analysts, and fans a practical tool for exploring data-driven play-calling.

