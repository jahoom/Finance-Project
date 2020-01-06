from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)
BAC_df = data.DataReader("BAC", 'stooq', start, end)
C_df = data.DataReader("C", 'stooq', start, end)
GS_df = data.DataReader("GS", 'stooq', start, end)
JPM_df = data.DataReader("JPM", 'stooq', start, end)
MS_df = data.DataReader("MS", 'stooq', start, end)
WFC_df = data.DataReader("WFC", 'stooq', start, end)


print("\nBank of America \n", BAC_df.head())
print("\nCitiGroup \n", C_df.head())
print("\nGoldman Sachs \n", GS_df.head())
print("\nJP Morgan \n", JPM_df.head())
print("\nMorgan Stanley \n", MS_df.head())
print("\nWells Fargo \n", WFC_df.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks = pd.concat([BAC_df, C_df, GS_df, JPM_df, MS_df, WFC_df], axis=1, keys = tickers)
bank_stocks.columns.names = ['Bank Ticker','Stock Info']
print(bank_stocks.head())
