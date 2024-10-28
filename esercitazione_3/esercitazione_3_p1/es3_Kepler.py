import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dopo aver scaricato il file dei dati in formato csv e salvato su una cartella, lo "importo" sul file tramite l'apposito comando della liberia di pandas

dataf_kepler = pd.read_csv('KeplerHAT-P-7 b.csv')

#provo a printare la tabella sul terminale sperando di non ottenere il caos

print(dataf_kepler)

#data frame viene stampato correttamente DAJEEEE


#tentativo di stampare i nomi delle colonne:

print(dataf_kepler.columns)


#la terza richiesta prevede la realizzazione di un grafico che fa vedere il cambiamento del flusso in funzione del tempo.
#dato che ho stampato i nomi delle colonne, so che la colonna del flusso è SAP_FLUX  a cui è associata un errore SAQP_FLUX_ERR, e inoltre la colonna del tempo è già disponibile.
#Allora procedo creando il grafico


#per prima cosa devo "estrarre" dal dataframe le colonne che mi servono:
# per farlo dovrò usare dataf_kepler['Nome colonna']

#GRAFICO 1 : NORMALE

plt.plot(dataf_kepler['TIME'], dataf_kepler['PDCSAP_FLUX'], color ='pink')

plt.xlabel('Time (s)')
plt.ylabel('Flux (e^- / s)')

plt.show()


#GRAFICO 2: PALLINI

plt.plot(dataf_kepler['TIME'], dataf_kepler['PDCSAP_FLUX'], 'o',  color ='pink')

plt.xlabel('Time (s)')
plt.ylabel('Flux (e^- / s)')

plt.show()

#GRAFICO 3: BARRE ERRORE

plt.errorbar(dataf_kepler['TIME'], dataf_kepler['PDCSAP_FLUX'],yerr=dataf_kepler['PDCSAP_FLUX_ERR'],fmt= 'o',  color ='pink')

plt.xlabel('Time (s)')
plt.ylabel('Flux (e^- / s)')

plt.show()




#GRAFICO 4: INTERVllO

#per creare il nuovo dataframe con l'intervallo corretto creo prima 3 array nulli che mi permettono di creare un dataframe vuoto

#ATTENAZIONE PER SCRIVERE & DEVI SCRIVERE AND (con la virgola)

data_minimo = dataf_kepler.loc[(dataf_kepler['TIME']> 939.2) & (dataf_kepler['TIME']<939.5)]

print(data_minimo)


plt.errorbar(data_minimo['TIME'], data_minimo['PDCSAP_FLUX'],yerr=data_minimo['PDCSAP_FLUX_ERR'],fmt= 'o',  color ='pink')

plt.xlabel('Time (s)')
plt.ylabel('Flux (e^- / s)')

plt.show()


#GRAFICO 5:

fig, ax = plt.subplots(figsize=(14,8))

plt.errorbar(dataf_kepler['TIME'], dataf_kepler['PDCSAP_FLUX'],yerr=dataf_kepler['PDCSAP_FLUX_ERR'],fmt= 'o',  color ='pink')

plt.xlabel('Time (s)')
plt.ylabel('Flux (e^- / s)')

ins_ax = ax.inset_axes([0.7,0.7, 0.3,0.3 ])
ins_ax.errorbar(data_minimo['TIME'], data_minimo['PDCSAP_FLUX'],yerr=data_minimo['PDCSAP_FLUX_ERR'],fmt= 'o',  color ='pink')




plt.show()
