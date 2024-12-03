import pandas as pd
import datetime
import time
market = "NVDA"; start = int(time.mktime(datetime.datetime(2022,1,1,0,0).timetuple())); end = int(time.mktime(datetime.datetime.now().timetuple()))
download = f"https://query1.finance.yahoo.com/v7/finance/download/{market}?period1={start}&period2={end}&interval=1d&events=history&includeAdjustedClose=true"
df = pd.read_csv(download)
print(df)

# pip install pandas
# pip install DateTime