import pandas as pd
import matplotlib.pyplot as plt
import os


class TechnicalIndicatorVisualizer:
    """
    A class to visualize various technical indicators for stock market data.
    """

    def __init__(self, file_path: str):
        """
        Initializes the TechnicalIndicatorVisualizer class.

        :param file_path: Path to the CSV file containing processed stock market data with indicators.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ Error: The file {file_path} does not exist.")

        self.file_path = file_path
        self.data = pd.read_csv(file_path, index_col="Date", parse_dates=True)

        # Extract file name (without extension) to create a dedicated folder
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        self.output_folder = os.path.join("stock_visualizations", file_name)
        os.makedirs(self.output_folder, exist_ok=True)

    def plot_moving_averages(self):
        """Plots stock closing price with SMA and EMA."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data["Close"], label="Close Price", color="black")
        plt.plot(self.data.index, self.data["SMA_20"], label="SMA (20)", linestyle="dashed", color="blue")
        plt.plot(self.data.index, self.data["EMA_20"], label="EMA (20)", linestyle="dashed", color="red")
        plt.title("Stock Price with SMA & EMA")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.savefig(f"{self.output_folder}/moving_averages.png")
        plt.show()

    def plot_rsi(self):
        """Plots the Relative Strength Index (RSI)."""
        plt.figure(figsize=(12, 4))
        plt.plot(self.data.index, self.data["RSI"], label="RSI", color="purple")
        plt.axhline(y=70, color="red", linestyle="dashed")  # Overbought level
        plt.axhline(y=30, color="green", linestyle="dashed")  # Oversold level
        plt.title("Relative Strength Index (RSI)")
        plt.xlabel("Date")
        plt.ylabel("RSI Value")
        plt.legend()
        plt.grid()
        plt.savefig(f"{self.output_folder}/rsi.png")
        plt.show()

    def plot_stochastic_oscillator(self):
        """Plots the Stochastic Oscillator (%K and %D)."""
        plt.figure(figsize=(12, 4))
        plt.plot(self.data.index, self.data["%K"], label="Stochastic %K", color="blue")
        plt.plot(self.data.index, self.data["%D"], label="Stochastic %D", color="red")
        plt.axhline(y=80, color="red", linestyle="dashed")  # Overbought level
        plt.axhline(y=20, color="green", linestyle="dashed")  # Oversold level
        plt.title("Stochastic Oscillator")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.legend()
        plt.grid()
        plt.savefig(f"{self.output_folder}/stochastic_oscillator.png")
        plt.show()

    def plot_macd(self):
        """Plots the MACD and Signal Line."""
        plt.figure(figsize=(12, 4))
        plt.plot(self.data.index, self.data["MACD"], label="MACD", color="blue")
        plt.plot(self.data.index, self.data["MACD_Signal"], label="Signal Line", color="red")
        plt.axhline(y=0, color="black", linestyle="dashed")  # Zero line
        plt.title("MACD (Moving Average Convergence Divergence)")
        plt.xlabel("Date")
        plt.ylabel("MACD Value")
        plt.legend()
        plt.grid()
        plt.savefig(f"{self.output_folder}/macd.png")
        plt.show()

    def plot_bollinger_bands(self):
        """Plots the stock price along with Bollinger Bands."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data["Close"], label="Close Price", color="black")
        plt.plot(self.data.index, self.data["Bollinger_Upper"], label="Upper Band", linestyle="dashed", color="red")
        plt.plot(self.data.index, self.data["Bollinger_Lower"], label="Lower Band", linestyle="dashed", color="blue")
        plt.fill_between(self.data.index, self.data["Bollinger_Lower"], self.data["Bollinger_Upper"], color="gray", alpha=0.2)
        plt.title("Bollinger Bands")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.savefig(f"{self.output_folder}/bollinger_bands.png")
        plt.show()

    def visualize_all(self):
        """Runs all visualization methods and saves all plots in the corresponding folder."""
        self.plot_moving_averages()
        self.plot_rsi()
        self.plot_stochastic_oscillator()
        self.plot_macd()
        self.plot_bollinger_bands()


# Example Usage
if __name__ == "__main__":
    input_file = input("Enter the processed CSV file path (e.g., processed_stock_data/IOC.NS_2020-01-01_to_2025-02-24.csv): ").strip()
    
    visualizer = TechnicalIndicatorVisualizer(input_file)
    visualizer.visualize_all()
