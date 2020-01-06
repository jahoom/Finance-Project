from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


"""
Pobieranie danych z internetu. Niestety nie pobiera w wymaganym zakresie...
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
"""
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']

bank_stocks = pd.read_pickle('all_banks')
print(bank_stocks.head())
returns = pd.DataFrame(index = bank_stocks.index)

print("Najwyzsze kursy zamkniecia:\n", bank_stocks.xs(key='Close',axis=1,level='Stock Info').max())
print("Zwroty: \n", returns.head(10))

print("BAC Return: ", (bank_stocks['BAC']['Close'][1] - bank_stocks['BAC']['Close'][0])/bank_stocks['BAC']['Close'][1])

for ticker in tickers:
	returns[ticker+" Return"] = bank_stocks[ticker]['Close'].pct_change()
	
print(returns.head())

print("\nNajlepszy wzrost:\n")
for ticker in returns:
	print("\t", ticker, "\t", (returns[returns[ticker]==returns[ticker].max()].index).date, "\t", returns[ticker].max())

print("\nNajgorszy spadek:\n")
for ticker in returns:
	print("\t", ticker, "\t", (returns[returns[ticker]==returns[ticker].min()].index).date, "\t", returns[ticker].min())

print("\nOdchylenia standardowe w kursach: ")

for ticker in returns:
	print("\n", ticker, "\t", returns[ticker].std())

print("\nA w roku 2015: ")

for ticker in returns:
	print("\n", ticker, "\t", returns[ticker][returns.index.year==2015].std())

#sns.pairplot(returns)
#g = sns.distplot(returns['MS Return'].dropna(axis=0, how='any'), kde=True, color='green', bins=1000)
#g = sns.distplot(returns['C Return'].dropna(axis=0, how='any'), kde=True, color='red', bins=1000)
#g.set_xlim([-0.4,0.8])
print(bank_stocks.reset_index())
sns.set_style('whitegrid')
#for ticker in tickers:
	#sns.lineplot(x="Date", y='Close', data = bank_stocks[ticker].reset_index(), legend='full')

#Do poprawienia
#BAC_aver = pd.DataFrame()
#BAC_aver['Date'] = (bank_stocks[(bank_stocks.index).year==2018]).index

print(BAC_aver.head(10))

plt.show()