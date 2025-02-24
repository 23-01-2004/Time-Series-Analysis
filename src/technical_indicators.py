import pandas as pd
import os


class TechnicalIndicators:
    """
    A class to calculate various technical indicators for stock market data.
    """

    def __init__(self, file_path: str):
        """
        Initializes the TechnicalIndicators class.

        :param file_path: Path to the CSV file containing stock market data.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Error: The file {file_path} does not exist.")
        
        self.file_path = file_path
        self.data = pd.read_csv(file_path, index_col="Date", parse_dates=True)

    def calculate_sma(self, window: int = 20):
        """
        Computes the Simple Moving Average (SMA).

        :param window: Lookback period for SMA.
        """
        self.data[f"SMA_{window}"] = self.data["Close"].rolling(window=window).mean()

    def calculate_ema(self, window: int = 20):
        """
        Computes the Exponential Moving Average (EMA).

        :param window: Lookback period for EMA.
        """
        self.data[f"EMA_{window}"] = self.data["Close"].ewm(span=window, adjust=False).mean()

    def calculate_rsi(self, window: int = 14):
        """
        Computes the Relative Strength Index (RSI).

        :param window: Lookback period for RSI.
        """
        delta = self.data["Close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        self.data["RSI"] = 100 - (100 / (1 + rs))

    def calculate_stochastic_oscillator(self, k_window: int = 14, d_window: int = 3):
        """
        Computes the Stochastic Oscillator.

        :param k_window: Lookback period for %K.
        :param d_window: Lookback period for %D (signal line).
        """
        low_min = self.data["Low"].rolling(window=k_window).min()
        high_max = self.data["High"].rolling(window=k_window).max()
        self.data["%K"] = ((self.data["Close"] - low_min) / (high_max - low_min)) * 100
        self.data["%D"] = self.data["%K"].rolling(window=d_window).mean()

    def calculate_macd(self, short_window: int = 12, long_window: int = 26, signal_window: int = 9):
        """
        Computes the Moving Average Convergence Divergence (MACD) and Signal Line.

        :param short_window: Short EMA period.
        :param long_window: Long EMA period.
        :param signal_window: Signal line EMA period.
        """
        short_ema = self.data["Close"].ewm(span=short_window, adjust=False).mean()
        long_ema = self.data["Close"].ewm(span=long_window, adjust=False).mean()
        self.data["MACD"] = short_ema - long_ema
        self.data["MACD_Signal"] = self.data["MACD"].ewm(span=signal_window, adjust=False).mean()

    def calculate_bollinger_bands(self, window: int = 20, num_std: int = 2):
        """
        Computes Bollinger Bands.

        :param window: Lookback period for the moving average.
        :param num_std: Number of standard deviations for the bands.
        """
        sma = self.data["Close"].rolling(window=window).mean()
        std_dev = self.data["Close"].rolling(window=window).std()
        self.data["Bollinger_Upper"] = sma + (num_std * std_dev)
        self.data["Bollinger_Lower"] = sma - (num_std * std_dev)

    def save_to_csv(self, output_folder: str = "./data/processed_stock_data"):
        """
        Saves the computed indicators to a new CSV file.

        :param output_folder: Folder where the CSV file will be saved.
        """
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, os.path.basename(self.file_path))
        self.data.to_csv(output_file)
        print(f"📂 Processed data saved to: {output_file}")

    def show_sample_data(self, rows: int = 5):
        """
        Displays a sample of the processed data.

        :param rows: Number of rows to display.
        """
        print(self.data.head(rows))


# Example Usage
if __name__ == "__main__":
    input_file = input("Enter the CSV file path (e.g., stock_data/IOC.NS_2020-01-01_to_2025-02-24.csv): ").strip()

    indicators = TechnicalIndicators(input_file)

    # Compute Indicators
    indicators.calculate_sma()
    indicators.calculate_ema()
    indicators.calculate_rsi()
    indicators.calculate_stochastic_oscillator()
    indicators.calculate_macd()
    indicators.calculate_bollinger_bands()

    # Show Sample Data
    indicators.show_sample_data()

    # Save Processed Data
    indicators.save_to_csv()
