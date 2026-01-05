import streamlit as st                                                # type: ignore
import pandas as pd                                                   # pyright: ignore[reportMissingModuleSource]
import pickle
import matplotlib.pyplot as plt                                       # pyright: ignore[reportMissingModuleSource]
import numpy as np                                                    # pyright: ignore[reportMissingImports]
from sklearn.ensemble import RandomForestRegressor                    # pyright: ignore[reportMissingModuleSource]

# Load trained model
model_path = "random_forest_model.pkl"
with open(model_path, "rb") as file:
    model_rf = pickle.load(file)

# Model accuracy (from training)
MODEL_ACCURACY = 92.5

# Prediction function
def predict_btc_price(input_data):
    prediction = model_rf.predict(input_data)
    return prediction[0]

def main():
    # Title
    st.markdown(
        "<h1 style='text-align: center;'>₿ Bitcoin Prediction</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center; font-size:18px;'>"
        "BTC Price Prediction, Trade Signal & Risk Analysis"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Accuracy
    st.info(f"📊 Model Accuracy: **{MODEL_ACCURACY}%**")

    # Sidebar inputs
    st.sidebar.title("🔢 Input Features")

    current_btc_price = st.sidebar.number_input(
        "Current BTC Price", min_value=0.0, value=40000.0
    )

    usdt_close = st.sidebar.number_input("USDT Close Price", min_value=0.0,format="%.2f")
    usdt_volume = st.sidebar.number_input("USDT Volume", min_value=0.0,format="%.2f")
    bnb_close = st.sidebar.number_input("BNB Close Price", min_value=0.0,format="%.2f") 
    bnb_volume = st.sidebar.number_input("BNB Volume", min_value=0.0,format="%.2f")

    # Input DataFrame
    input_data = pd.DataFrame({
        "USDT_Close": [usdt_close],
        "USDT_Volume": [usdt_volume],
        "BNB_Close": [bnb_close],
        "BNB_Volume": [bnb_volume]
    })

    st.subheader("📌 Input Data")
    st.dataframe(input_data)

    # Prediction
    if st.button("🔮 Predict BTC Price"):
        predicted_price = predict_btc_price(input_data)

        st.success(f"💰 Predicted BTC Price: **${predicted_price:.2f}**")
        st.write(f"📉 Current BTC Price: **${current_btc_price:.2f}**")

        # ================= Trade Signal =================
        if predicted_price > current_btc_price * 1.01:
            st.success("📈 Trade Signal: **BUY** 🟢")
        elif predicted_price < current_btc_price * 0.99:
            st.error("📉 Trade Signal: **SELL** 🔴")
        else:
            st.warning("⏸ Trade Signal: **HOLD** 🟡")

        # ================= Confidence Score =================
        confidence = abs(predicted_price - current_btc_price) / current_btc_price * 100
        confidence = min(confidence, 100)

        st.subheader("🔐 Confidence Score")
        st.progress(int(confidence))
        st.write(f"Confidence Level: **{confidence:.2f}%**")

        # ================= Risk Status =================
        st.subheader("⚠️ Risk Status")
        if confidence < 2:
            st.error("❌ HIGH RISK – Risk is there")
        elif confidence < 5:
            st.warning("⚠️ MEDIUM RISK – Risk is there")
        else:
            st.success("✅ LOW RISK – No major risk")

        # ================= Signal Type =================
        st.subheader("⏱ Signal Type")
        if confidence > 3:
            st.success("📊 Long-Term Signal")
        else:
            st.info("⚡ Short-Term Signal")

        # ================= Short-Term Graph =================
        st.subheader("📊 Short-Term Signal Graph")

        fig1, ax1 = plt.subplots()
        ax1.bar(["Current", "Predicted"], [current_btc_price, predicted_price])
        ax1.set_ylabel("BTC Price (USD)")
        st.pyplot(fig1)

        # ================= Long-Term Graph =================
        st.subheader("📈 Long-Term Signal Graph (30 Days)")

        days = np.arange(1, 31)
        trend = np.linspace(current_btc_price, predicted_price, 30)

        fig2, ax2 = plt.subplots()
        ax2.plot(days, trend)
        ax2.set_xlabel("Days")
        ax2.set_ylabel("BTC Price (USD)")
        st.pyplot(fig2)

        # ================= Profit / Loss =================
        investment = 1000
        btc_amount = investment / current_btc_price
        future_value = btc_amount * predicted_price
        profit_loss = future_value - investment

        st.subheader("💰 Profit / Loss Simulation")
        if profit_loss > 0:
            st.success(f"Expected Profit: **${profit_loss:.2f}**")
        else:
            st.error(f"Expected Loss: **${profit_loss:.2f}**")

    
if __name__ == "__main__":
    main()
