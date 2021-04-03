import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import math

ricampionato1 = pd.DataFrame()
ricampionato2 = pd.DataFrame()
ftse100= pd.DataFrame()
euro50 = pd.DataFrame()


#definisco un dataframe nuovo
df2 = pd.DataFrame()

#definizione data inizio rilevazione
start = dt.datetime(2010,1,1)

#definizione data fine rilevazione
end = dt.datetime(2020,11,30)

#Download delle serie storiche di Ferrari e Recordati
df1 = web.DataReader("FEZ", "yahoo", start, end)
df2 = web.DataReader("ISFA.AS", "yahoo", start, end)

#ricampionamento menisle titoli
ricampionato1 = df1.resample("MS").first()
ricampionato2 = df2.resample("MS").first()

#calcolo dei rendimenti percentuale dei titoli
ftse100["Rendimenti"] = ricampionato1["Adj Close"].pct_change()
euro50["Rendimenti"] = ricampionato2["Adj Close"].pct_change()

#rimozione dei valori NaN
ftse100.dropna(inplace = True)
euro50.dropna(inplace = True)

#Calcolo della media dei rendimenti
mediaftse100 = ftse100["Rendimenti"].mean()
mediaeuro50 = euro50["Rendimenti"].mean()

#Calcolo della varianza dei rendimenti
varianzaftse100 = ftse100["Rendimenti"].var()
varianzaeuro50 = euro50["Rendimenti"].var()

#Calcolo della deviazione standard
devftse100 = math.sqrt(varianzaftse100)
deveuro50 = math.sqrt(varianzaeuro50)

#Calcolo della correlazione
corr = ftse100["Rendimenti"].corr(euro50["Rendimenti"])

ponderazione1 = 1
ponderazione2 = 0
x = 0

while x <= 50:
    rischiosita = (ponderazione1 * devftse100)**2 + (ponderazione2 * deveuro50)**2 + 2 * ponderazione1 * ponderazione2 * devftse100 * deveuro50 * corr
    rischiosita_portafoglio = math.sqrt(rischiosita)
    rend_portafoglio = mediaftse100 * ponderazione1 + mediaeuro50 * ponderazione2
    ponderazione1 = ponderazione1 - 0.02
    ponderazione2 = ponderazione2 + 0.02
    x+=1
    plt.scatter(rischiosita_portafoglio, rend_portafoglio, color="k", s=10)

plt.xlabel("Deviazione standard")
plt.ylabel("Rendimento atteso")
plt.title("Frontiera efficiente")
plt.show()







