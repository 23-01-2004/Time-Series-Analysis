import yfinance as yf
import pandas as pd
import os
from datetime import datetime


class StockDataFetcher:
    """
    A class to fetch and save historical stock market data from Yahoo Finance.
    """

    def __init__(self, symbol: str, start_date: str, end_date: str):
        """
        Initializes the StockDataFetcher class.

        :param symbol: The stock symbol (e.g., 'IOC.NS' for Indian Oil Corporation).
        :param start_date: The start date for fetching historical data (YYYY-MM-DD format).
        :param end_date: The end date for fetching historical data (YYYY-MM-DD format).
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def fetch_data(self):
        """
        Fetches historical stock data from Yahoo Finance, excluding dividends and stock splits.
        """
        try:
            stock = yf.Ticker(self.symbol)
            self.data = stock.history(start=self.start_date, end=self.end_date)
            
            if self.data.empty:
                raise ValueError(f"No data found for {self.symbol} in the given date range.")

            # Keep only relevant columns (Open, High, Low, Close, Volume)
            self.data = self.data[['Open', 'High', 'Low', 'Close', 'Volume']]

            print(f"✅ Successfully fetched data for {self.symbol}.")
        except Exception as e:
            print(f"❌ Error fetching data: {e}")

    def save_to_csv(self, folder_path: str = "data"):
        """
        Saves the fetched stock data as a CSV file.

        :param folder_path: The folder where the CSV file will be saved.
        """
        if self.data is not None:
            os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
            file_path = os.path.join(folder_path, f"{self.symbol}_{self.start_date}_to_{self.end_date}.csv")
            self.data.to_csv(file_path)
            print(f"📂 Data saved to: {file_path}")
        else:
            print("⚠️ No data to save. Fetch data first.")

    def show_sample_data(self, rows: int = 5):
        """
        Displays a sample of the fetched stock data.

        :param rows: Number of rows to display.
        """
        if self.data is not None:
            print(self.data.head(rows))
        else:
            print("⚠️ No data available. Fetch data first.")


# Example Usage
if __name__ == "__main__":
    stock_symbol = input("Enter NSE stock symbol (e.g., IOC.NS): ").strip().upper()
    start_date = "2015-01-01"
    end_date = datetime.today().strftime('%Y-%m-%d')

    fetcher = StockDataFetcher(stock_symbol, start_date, end_date)
    fetcher.fetch_data()
    fetcher.show_sample_data()
    fetcher.save_to_csv()
