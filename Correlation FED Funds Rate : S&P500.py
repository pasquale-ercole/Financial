import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import math

df3 = pd.DataFrame()
df4 = pd.DataFrame()

start = dt.datetime(2010,1,1)
end = dt.datetime(2020,11,30)

df1 = web.DataReader("FEZ", "yahoo", start, end)
df2 = web.DataReader("ISFA.AS", "yahoo", start, end)
corr = df1["Adj Close"].corr(df2["Adj Close"])
                        
#Calcolo dei rendimenti del FTSE100 ed EUROSTOCK50
df3["Rendimenti"] = df1["Adj Close"].pct_change()
df4["Rendimenti"] = df2["Adj Close"].pct_change()
#Rimozione degli elementi NaN per calcolare opportunamente la correlazione
df3.dropna(inplace = True)
df4.dropna(inplace = True)

#Calcolo la correlazione dei due ticker

corr2 = df3["Rendimenti"].corr(df4["Rendimenti"])
print(corr2)

plt.plot(df3, label = "Eurostock 50")
plt.plot(df4, label = "FTSE100")
plt.title("Eurostock50 and FTSE100")
plt.grid()
plt.legend()
plt.show()

