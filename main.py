import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download("MSFT", start="2020-01-01", end="2021-01-01")
data['Close'].plot()
plt.title("Apple Stock Prices")
plt.show()