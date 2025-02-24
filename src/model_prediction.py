import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import os

class StockPredictor:
    def __init__(self, csv_file):
        """
        Initializes the StockPredictor with a CSV file.

        :param csv_file: Path to the stock data CSV file.
        """
        self.csv_file = csv_file
        self.df = self._load_data()
        self.model = Prophet()

    def _load_data(self):
        """
        Loads and preprocesses the stock data for Prophet.

        - Reads the CSV file.
        - Ensures necessary columns exist.
        - Converts the 'Date' column to datetime and removes timezone.
        - Drops missing values.

        :return: Processed DataFrame.
        """
        df = pd.read_csv(self.csv_file)

        # Ensure required columns exist
        required_cols = {'Date', 'Close'}
        missing_cols = required_cols - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in CSV file: {missing_cols}")

        # Select necessary columns
        df = df[['Date', 'Close']]  # Prophet requires 'ds' (date) and 'y' (target)

        # Convert 'Date' column to datetime and remove timezone
        df.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
        df['ds'] = pd.to_datetime(df['ds'], errors='coerce')
        df['ds'] = df['ds'].dt.tz_localize(None)  # Remove timezone if present

        # Drop any rows with missing values
        df.dropna(inplace=True)

        return df

    def train_model(self):
        """
        Trains the Prophet model on the stock data.
        """
        self.model.fit(self.df)

    def predict(self, future_days=365):
        """
        Predicts stock prices for the next given number of days.

        :param future_days: Number of days to predict into the future.
        :return: DataFrame with predictions.
        """
        future = self.model.make_future_dataframe(periods=future_days)
        forecast = self.model.predict(future)
        return forecast

    def plot_forecast(self, forecast, save_path="stock_forecast/forecast_plot.png"):
        """
        Plots the forecasted stock prices with improved visualization.

        :param forecast: DataFrame containing predictions.
        :param save_path: Path to save the forecast plot.
        """
        # Create directory if not exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        plt.figure(figsize=(14, 7))
        sns.set_style("darkgrid")

        # Plot actual prices
        plt.plot(self.df['ds'], self.df['y'], label="Actual Prices", color='#1f77b4', linewidth=2)

        # Plot predicted prices
        plt.plot(forecast['ds'], forecast['yhat'], label="Predicted Prices", color='#d62728', linewidth=2)

        # Confidence interval shading
        plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='pink', alpha=0.3)

        # Title and labels
        plt.xlabel("Date", fontsize=12, fontweight='bold')
        plt.ylabel("Stock Price", fontsize=12, fontweight='bold')
        plt.title("Stock Price Forecast using Prophet", fontsize=14, fontweight='bold')

        # Highlight last actual and first predicted points
        plt.scatter(self.df['ds'].iloc[-1], self.df['y'].iloc[-1], color='blue', s=100, edgecolor='black', label="Last Actual Price")
        plt.scatter(forecast['ds'].iloc[-365], forecast['yhat'].iloc[-365], color='red', s=100, edgecolor='black', label="First Forecasted Price")

        # Rotate x-axis labels
        plt.xticks(rotation=45)

        # Add legend
        plt.legend(fontsize=11)

        # Save and show the plot
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        print(f"Forecast plot saved as {save_path}")

    def save_forecast(self, forecast, output_file="stock_forecast/forecast.csv"):
        """
        Saves the forecasted stock prices to a CSV file.

        :param forecast: DataFrame containing predictions.
        :param output_file: Name of the output CSV file.
        """
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        forecast.to_csv(output_file, index=False)
        print(f"Forecast saved as {output_file}")

# ✅ Example Usage:
predictor = StockPredictor(r"data\processed_stock_data\wipro_ns.csv")
predictor.train_model()
forecast = predictor.predict(365)  # Predict for 1 year
predictor.plot_forecast(forecast, "stock_forecast/wipro_forecast.png")
predictor.save_forecast(forecast, "stock_forecast/wipro_forecast.csv")

# Display first few rows of predictions
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
