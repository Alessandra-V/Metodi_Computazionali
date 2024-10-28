import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importo il file richiesto sul dataframe

exopl = pd.read_csv('ExoplanetsPars_2024.csv', comment= '#')

print(exopl)

print(exopl.columns)

print(exopl.iloc[123:130])

#exopl['pl_orbper']
#exopl['bmassj']

plt.scatter(exopl['pl_orbper'],exopl['pl_bmassj'], color = 'violet' )

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Orbital Period [Days]')
plt.ylabel('Planet Mass [Jupiter Mass]')

plt.show()


#PUNTO 5:

arr1 =( (exopl['pl_orbsmax'])**2)/exopl['st_mass']

plt.scatter(exopl['pl_orbper'],arr1, color = 'violet' )

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Orbital Period [Days]')
plt.ylabel('R^2_max/m* [au^2/ Solar Mass]')

plt.show()


#PUNTO 6:

exopl_transit = exopl.loc[(exopl['discoverymethod']== 'Transit' )]
exopl_radial = exopl.loc[(exopl['discoverymethod']=='Radial Velocity')]


plt.scatter(exopl_transit['pl_orbper'], exopl_transit['pl_bmassj'], label= 'Transit', alpha = 0.4, color = 'violet' )
plt.scatter(exopl_radial['pl_orbper'], exopl_radial['pl_bmassj'], label = 'Radial Velocity' ,  alpha = 0.4, color = 'orange')

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Orbital Period [Days]')
plt.ylabel('Planet Mass [JUpiter  Mass]')

plt.legend()
plt.show()
