import matplotlib.pyplot as plt
import yfinance as yf

# get stock data
data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
data['Close'].plot()
plt.title("Apple Stock Prices")
plt.show()