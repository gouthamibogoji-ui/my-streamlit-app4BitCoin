This project is a A Streamlit-based Machine Learning web application that predicts Bitcoin (BTC) price, generates trade signals, and performs volatility-based risk analysis using a Random Forest Regressor.
This project is designed for learning, portfolio analysis, and ML-based trading insights.

## Features
- Bitcoin price prediction using a trained Random Forest model  
- BUY / SELL / HOLD trade signal generation  
- Model confidence score  
- Volatility-based risk analysis  
- Short-term and long-term price visualizations  
- Profit / Loss simulation  
- Interactive Streamlit dashboard  

## Machine Learning Model
- Algorithm: Random Forest Regressor  
- Model Accuracy: 92.5% (training accuracy)  
- Saved Model File: `random_forest_model.pkl`  

## Input Features
The model predicts BTC price using the following market features:

| Feature Name | Description        |
|------------- |--------------------|
| USDT_Close   | USDT closing price |
| USDT_Volume  | USDT trading volume|
| BNB_Close    | BNB closing price  |
| BNB_Volume   | BNB trading volume |

## Trade Signal Logic

| Condition                            | Signal |
|--------------------------------------|--------|
| Predicted Price > Current Price + 1% | BUY    |
| Predicted Price < Current Price − 1% | SELL   |
| Otherwise                            | HOLD   |

### Risk Classification
| Volatility (%) | Risk Level |
|----------------|------------|
| < 3%           | Low Risk   |
| 3% – 6%        | Medium Risk|
| > 6%           | High Risk  |

The application clearly indicates whether **risk is present or not**.

## Visualizations
- Short-term price comparison (Current vs Predicted)  
- 30-day long-term trend projection  
- Volatility meter  
- Profit / Loss simulation

## Tech Stack
- Python  
- Streamlit  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn

## Installation & Usage

### Clone the Repository
git clone https://github.com/gouthamibogoji-ui/my-streamlit-app4BitCoin.git
cd my-streamlit-app4BitCoin

### Install Dependencies
pip install -r requirements.txt

### Run the Application
streamlit run app.py

## Project Structure
my-streamlit-app4BitCoin/
│
├── cryptoanalysisapp.py
├── random_forest_model.pkl
├── requirements.txt
└── README.md

## Author
Gouthami Bogoji  
