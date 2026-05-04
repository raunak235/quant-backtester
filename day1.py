import yfinance as yf

data = yf.download("RELIANCE.NS", start="2024-01-01")
print(data.tail())