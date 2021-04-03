import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import math

df3 = pd.DataFrame()
df4 = pd.DataFrame()

#definisco un dataframe nuovo
df2 = pd.DataFrame()

#definizione data inizio rilevazione
start = dt.datetime(2016,1,22)

#definizione data fine rilevazione
end = dt.datetime(2021,1,22)

#Download delle serie storiche del titolo da valutare e del Benchmark
df = web.DataReader("INTC", "yahoo", start, end)
df2 = web.DataReader("^GSPC", "yahoo", start, end)

#calcolo dei rendimenti del asset e del benchmark
df3["Rendimenti"] = df["Adj Close"].pct_change()
df4["Rendimenti"] = df2["Adj Close"].pct_change()

#eliminati gli elementi NaN
df3.dropna(inplace = True)
df4.dropna(inplace = True)

#Calcolo coviarianza della security e del benchmark
cov = df3["Rendimenti"].cov(df4["Rendimenti"])

#calcolo della varianza del asset
varnasq = df4["Rendimenti"].var()

#Calcolo del Beta come rapporto fra la coviarianza dei due oggetti e la varianza della security
beta = cov/varnasq
print("Il Beta del titolo in riferimento all'indice S&P500 è " + str(beta))
