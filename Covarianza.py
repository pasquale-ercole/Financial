import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import math

#definisco un dataframe nuovo
df2 = pd.DataFrame()

#definizione data inizio rilevazione
start = dt.datetime(2018,1,1)

#definizione data fine rilevazione
end = dt.datetime(2020,12,10)

#Download delle serie storiche di Ferrari e Tesla
df = web.DataReader("^GSPC", "yahoo", start, end)
df2 = web.DataReader("TSLA", "yahoo", start, end)

cov = df["Adj Close"].cov(df2["Adj Close"])

print("La covarianza fra S&P e Tesla è " + str(cov))


                     





