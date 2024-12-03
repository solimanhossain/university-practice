import yfinance
df = yfinance.download('NVDA')
# df = yf.Ticker("NVDA").history(period="1y")
print(df)

# pip install yfinance --upgrade --no-cache-dir
# pip install DateTime