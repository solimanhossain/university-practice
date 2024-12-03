import quandl
import quandl
# data = quandl.get_table('ZACKS/FC', ticker='AAPL')
df = quandl.get('WIKI/NVDA', authtoken='your_api_key')
print(df)

# pip install quandl
# pip install DateTime