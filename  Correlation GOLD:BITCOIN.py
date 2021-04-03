import pandas as pd
import pandas_datareader.data as web
import datetime as dt

df3 = pd.DataFrame()
df4 = pd.DataFrame()

start = dt.datetime(2016,1,1)
end = dt.datetime(2020,12,23)

df = web.DataReader("BTC-USD", "yahoo", start, end)
df2 = web.DataReader("^GSPC", "yahoo", start, end)

#Calcolo dei rendimenti di FB e EXXON
df3["Rendimenti"] = df["Adj Close"].pct_change()
df4["Rendimenti"] = df2["Adj Close"].pct_change()

#Rimozione degli elementi NaN per calcolare opportunamente la correlazione
df3.dropna(inplace = True)
df4.dropna(inplace = True)

corr = df3["Rendimenti"].corr(df4["Rendimenti"])

print(corr)
