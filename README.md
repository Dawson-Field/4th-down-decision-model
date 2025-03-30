# 4th Down Decision Assistant

This project uses a machine learning model trained on historical NFL play-by-play data to help NFL teams decide whether to go for it, punt, or kick a field goal on 4th down.

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

## Live App

Try it here: [4th Down Decision Assistant](https://dawsonfield-4th-down-decision-model.hf.space)

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
