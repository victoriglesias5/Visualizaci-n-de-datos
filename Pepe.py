#Importamos todas las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

#Leemos nuestro dataframe e imprimimos para tener una primera toma de contacto
df = pd.read_csv('Accidents2.csv')
df.head(10)
df.shape

#Creamos las variables categóricas
lista_cat = ['Special_Conditions_at_Site', 'Pedestrian_Crossing-Physical_Facilities','Light_Conditions',
             'Junction_Control','Road_Type','Carriageway_Hazards','Road_Surface_Conditions',
             'Pedestrian_Crossing-Human_Control', 'Weather_Conditions', 'Did_Police_Officer_Attend_Scene_of_Accident']
df[lista_cat] = df[lista_cat].astype('category')
df.dtypes

"""Index(['Year', 'Date', 'Day_of_Week', 'Hour', 'Mes', 'Estacion',
       'Accident_Severity', 'Number_of_Vehicles', 'Number_of_Casualties',
       'Road_Type', 'Speed_limit', 'Junction_Control',
       'Pedestrian_Crossing-Human_Control',
       'Pedestrian_Crossing-Physical_Facilities', 'Light_Conditions',
       'Weather_Conditions', 'Road_Surface_Conditions',
       'Special_Conditions_at_Site', 'Carriageway_Hazards',
       'Did_Police_Officer_Attend_Scene_of_Accident'],
      dtype='object')
"""

#Weather conditions con accident severity

# Graficos de las variables por separado
# Accident_Sev, "Special_Cond", "Pedestrian_Crossing", "Hour", "Year", "Police_Force", "Light Conditions"

# plot bar por años

value_counts = df["Year"].value_counts()
bars = plt.bar(value_counts.index, value_counts.values)
plt.xlabel("Año")
plt.ylabel("Número de accidentes")
plt.title("Accidentes por año")
plt.show()

#plot bar light conditions. La mayoría de accidentes ocurren cuando existe claridad de luz, no existe una relación entre uno y otro
value_counts = df["Light_Conditions"].value_counts()
bars = plt.bar(value_counts.index, value_counts.values)
plt.xlabel("Condiciones Luminosas")
plt.xticks (rotation = 90)
plt.ylabel("Numero de accidentes")
plt.show()
 
# #plot bar accident severity. Aquí, fatal es 1, serious es 2 y 3 sin mayores consecuencias
# value_counts = df["Accident_Severity"].value_counts()
# pies = plt.pie(x= value_counts.values, labels = value_counts.index, autopct='%2.2f%%')
# #plt.legend(zip(value_counts.index, value_counts.values), title='Category Counts', loc='upper left', bbox_to_anchor=(1, 0.5))
# plt.show()

#comparación de accident severity con speed limit
sns.violinplot(x=df['Accident_Severity'], y=df['Speed_limit'])
plt.show()
