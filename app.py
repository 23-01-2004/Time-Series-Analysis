import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet

# Streamlit Page Configuration
st.set_page_config(page_title="Stock Price Prediction", layout="wide")

# Title of the App
st.title("📈 Stock Price Prediction using Prophet")

# Upload CSV File
uploaded_file = st.file_uploader("Upload Stock Data CSV (Date, Close)", type=['csv'])

# Prediction Days Input
future_days = st.slider("Select Number of Days to Predict", min_value=30, max_value=730, value=365)

if uploaded_file:
    # Load Data
    df = pd.read_csv(uploaded_file)

    # Ensure necessary columns
    required_cols = {'Date', 'Close'}
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        st.error(f"Missing columns: {missing_cols}. Ensure CSV contains 'Date' and 'Close'.")
    else:
        # Preprocess Data
        df = df[['Date', 'Close']]
        df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
        df['ds'] = pd.to_datetime(df['ds'], errors='coerce')
        df['ds'] = df['ds'].dt.tz_localize(None)  # Remove timezone if present
        df.dropna(inplace=True)

        # Display Raw Data
        st.subheader("📊 Raw Data Preview")
        st.dataframe(df.head())

        # Train Prophet Model
        model = Prophet()
        model.fit(df)

        # Predict Future Prices
        future = model.make_future_dataframe(periods=future_days)
        forecast = model.predict(future)

        # Plot Forecast
        st.subheader("📉 Stock Price Forecast")
        plt.figure(figsize=(12, 6))
        sns.set_style("darkgrid")

        plt.plot(df['ds'], df['y'], label="Actual Prices", color='blue', linewidth=2)
        plt.plot(forecast['ds'], forecast['yhat'], label="Predicted Prices", color='red', linewidth=2)
        plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='pink', alpha=0.3)
        plt.xlabel("Date", fontsize=12, fontweight='bold')
        plt.ylabel("Stock Price", fontsize=12, fontweight='bold')
        plt.title("Stock Price Forecast using Prophet", fontsize=14, fontweight='bold')
        plt.xticks(rotation=45)
        plt.legend(fontsize=11)
        st.pyplot(plt)

        # Download Forecast CSV
        st.subheader("📥 Download Forecast Data")
        forecast_csv = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(index=False).encode('utf-8')
        st.download_button(label="Download Forecast CSV", data=forecast_csv, file_name="forecast.csv", mime="text/csv")

