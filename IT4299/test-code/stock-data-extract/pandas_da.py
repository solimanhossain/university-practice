import pandas_datareader.data as pdr
df = pdr.DataReader('IBM','yahoo')
# pdr.get_data_yahoo('IBM')
print(df)

# pip install pandas_datareader
# pip install --upgrade pandas-datareader