This project is a A Streamlit-based Machine Learning web application that predicts Bitcoin (BTC) price, generates trade signals, and performs volatility-based risk analysis using a Random Forest Regressor.
This project is designed for learning, portfolio analysis, and ML-based trading insights.

## Features:
✔ Bitcoin Price Prediction using Random Forest
✔ Trade Signal Detection (BUY / SELL / HOLD)
✔ Model Confidence Score
✔ Volatility-Based Risk Analysis
✔ Short-Term & Long-Term Price Visualization
✔ Profit / Loss Simulation
✔ Clean & Interactive Streamlit UI

## Machine Learning Model:
Algorithm: Random Forest Regressor
Training Data: Crypto market features (USDT & BNB)
Model Accuracy: 92.5% (Training Accuracy)
Saved Model: random_forest_model.pkl,scalar.pkl

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
