# 📌 Stock Price Prediction using Prophet & Streamlit
# 📈 Forecast stock prices with ease using Facebook's Prophet model!

# 📜 Overview
This is a machine learning-based stock price prediction application built using:

📊 Facebook Prophet for time-series forecasting
🎨 Streamlit for an interactive user interface
📉 Matplotlib & Seaborn for beautiful visualizations
It allows users to upload stock market data (CSV), preprocess it, train a Prophet model, and visualize future stock price trends.

# 🚀 Features
✔ Upload Stock Data (CSV format)
✔ Data Preprocessing (Handling missing values & timezone conversion)
✔ Stock Price Forecasting (Using Prophet model)
✔ Interactive Visualizations (Trend & Confidence Intervals)
✔ Download Forecasted Data

# 🛠 Installation
🔹 Prerequisites
Make sure you have Python 3.7+ installed.

# 🔹 Install Dependencies
Run the following command to install all required libraries:


pip install streamlit prophet matplotlib seaborn pandas
# 🔹 Clone the Repository

git clone https://github.com/23-01-2004/Time-Series-Analysis.git
cd Time-Series-Analysis
📂 Folder Structure
📁Time-Series-Analysis
│── 📂 data
│   └── processed_stock_data.csv
│── 📂 stock_forecast
│   ├── wipro_forecast.csv
│   └── wipro_forecast.png
│── app.py
│── README.md
└── requirements.txt
# 🎯 How to Use
Step 1️⃣: Run the Streamlit App

streamlit run app.py
This will open the web app in your browser.

Step 2️⃣: Upload a Stock Data CSV
Ensure your CSV has 'Date' and 'Close' columns.
Example format:
Date	Close
2024-01-01	1500
2024-01-02	1525
Step 3️⃣: Train the Model & Forecast
The Prophet model will train automatically.
Predictions will be made for 1 year ahead.
Step 4️⃣: Visualize Predictions
Blue Line → Actual Stock Prices
Red Line → Predicted Prices
Shaded Region → Confidence Interval
Step 5️⃣: Download the Forecast
You can download the forecasted stock prices as a CSV.



# ⚙️ Technologies Used
Python 🐍
Streamlit (Web UI)
Facebook Prophet (Time-Series Forecasting)
Matplotlib & Seaborn (Data Visualization)
Pandas (Data Processing)
📌 Future Enhancements
🔹 Add support for multiple stock symbols 📊
🔹 Implement real-time stock price updates ⏳
🔹 Deploy the app using Streamlit Cloud / Heroku ☁

# 🤝 Contributing
Want to improve this project? Follow these steps:

# Fork the repo
Create a new branch (git checkout -b feature-xyz)
Commit changes (git commit -m "Added new feature")
Push to branch (git push origin feature-xyz)
Open a Pull Request 🚀
# 📜 License
This project is licensed under the MIT License.

💬 Need Help?
📩 Contact me 23subhasmukherjee@gmail.com

# 🚀 Happy Forecasting! 🎯