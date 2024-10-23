import matplotlib.pyplot as plt
import yfinance as yf

# get stock data
data = yf.download(["MSFT","AAPL"], start="2020-01-01", end="2021-01-01")


data['Close'].plot()
plt.title("Microsoft and Apple Stock Prices")
plt.show()