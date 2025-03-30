# 4th Down Decision Assistant

This project uses a machine learning model trained on historical NFL play-by-play data to help offensive teams decide whether to go for it, punt, or kick a field goal on 4th down.

## 🧠 How It Works

- Built using `nfl_data_py`, `pandas`, and `PyCaret`
- Trained on past seasons and tested on 2024 data
- Predicts the optimal 4th down decision based on:
  - Field position
  - Yards to go
  - Score differential
  - Time remaining
  - Quarter
  - Timeouts

## 🔗 Live App

Try it here: [4th Down Decision Assistant](https://dawsonfield-4th-down-decision-model.hf.space)

## 📓 Interactive Notebook

Explore the full modeling process, data cleaning, and visualizations in Google Colab:  
[Colab Notebook](https://colab.research.google.com/drive/YOUR_SHAREABLE_COLAB_LINK)

## 💡 Built With

- [PyCaret](https://pycaret.org/) for training and comparing classification models
- [nfl_data_py](https://github.com/nflverse/nfl_data_py) for play-by-play NFL data
- [Streamlit](https://streamlit.io/) for deployment
- [Hugging Face Spaces](https://huggingface.co/spaces) for hosting

## 👨‍💻 Author

Built by **Dawson Field**  
[LinkedIn](https://www.linkedin.com/in/dawson-field)
