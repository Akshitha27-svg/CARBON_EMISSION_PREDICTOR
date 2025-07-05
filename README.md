# 🌍 CO₂ Emission Predictor

A local Python application that predicts **CO₂ emissions (in tons per capita)** using a machine learning model trained on various climate and economic indicators.

Link to the Model: https://drive.google.com/file/d/1R08mOGPySz174lsbmb5J5W52HTeegP_L/view?usp=sharing

 COPY AND PASTE IT IN YOUR BROWSER YOU CAN DOWNLOAD THE MODEL
## 📌 Project Description

This application:
- Loads a pre-trained ML model (`.pkl.bz2` format).
- Takes **7 comma-separated numerical inputs** from the user.
- Predicts per capita CO₂ emissions based on the input features.

It runs entirely **locally** through a command-line interface (CLI), with future potential for web integration (e.g., using Flask).

---

## 📁 Project Structure project-folder/
project-folder/
├── forecasting_co2_emmision.pkl.bz2 # Compressed trained model file
├── app.py # CLI app for local prediction
├── data_cleaned (1).csv # Cleaned dataset
├── climate_change_download_0 (2).xls # Original data source
├── data_exploration.ipynb # Notebook for EDA
├── data_preparation.ipynb # Notebook for preprocessing
├── model_building.ipynb # Notebook for model training
└── README.md # Documentation

---

## 🧠 Model Overview

The model was trained using:
- `scikit-learn` regression algorithms
- 7 features:
  1. GDP per capita
  2. Energy consumption per capita
  3. Urban population (%)
  4. Total population
  5. Renewable energy usage (%)
  6. CO₂ intensity of energy
  7. Industry emissions per capita

The final model was saved and compressed as:  
`forecasting_co2_emmision.pkl.bz2`

---

## 💡 How It Works

- You run the `app.py` script.
- It prompts you to enter 7 comma-separated values.
- The model predicts CO₂ emission (in tons per capita).

---

## 🛠️ Requirements

**Make sure Python 3.7+ is installed.**

Install the required libraries:

**pip install numpy joblib**

# How to Run the App
Open your terminal and run:

**python app.py**

📊 CO₂ Emission Predictor (Local Version)
Enter 7 comma-separated input features (e.g., 45000, 3200, 78, 1400000000, 25, 0.26, 1.4):
Type the input and get a prediction instantly.
Type exit or quit to end the app.

📊 Jupyter Notebooks
data_exploration.ipynb – Visualizes relationships and patterns in raw data.

data_preparation.ipynb – Cleans and prepares the dataset.

model_building.ipynb – Trains and evaluates machine learning models.

Run notebooks using:


**jupyter notebook**

Example Input**

**Input: 45000, 3200, 78, 1400000000, 25, 0.26, 1.4  
Output: Predicted CO₂ Emission: 6.52 tons per capita**

Author
Chintakunta Akshitha
📄 License
This project is open-source and intended for educational and research use only.


