from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)
BAC_df = data.DataReader("BAC", 'stooq', start, end)

print(BAC_df.head())