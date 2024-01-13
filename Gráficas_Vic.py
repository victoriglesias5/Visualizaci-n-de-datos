#['Road_Type', '2nd_Road_Number', 'Number_of_Casualties', 'LSOA_of_Accident_Location',
#'Weather_Conditions', 'Number_of_Vehicles', 'Speed_limit', 'Latitude']

#Importamos todas las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

df = pd.read_csv('UK_Accident.csv')

#Representamos los datos de la columna Road_Type
df['Road_Type'].value_counts().plot(kind='bar')
plt.title('Road_Type')
plt.show()

#Representamos los datos de la columna Police_Force
df['Police_Force'].value_counts().plot(kind='bar')
plt.title('Police_Force')
plt.show()

#Representamos los datos de la columna Accident_Severity
df['Accident_Severity'].value_counts().plot(kind='bar')
plt.title('Accident_Severity')
plt.show()

#Representamos los datos de la columna Number_of_Vehicles
df['Number_of_Vehicles'].value_counts().plot(kind='bar')
plt.title('Number_of_Vehicles')
plt.show()

#Representamos los datos de la columna Number_of_Casualties
df['Number_of_Casualties'].value_counts().plot(kind='bar')
plt.title('Number_of_Casualties')
plt.show()

#Representamos los datos de la columna Weather_Conditions
df['Weather_Conditions'].value_counts().plot(kind='bar')
plt.title('Weather_Conditions')
plt.show()

#Representamos los datos de la columna Speed_limit
df['Speed_limit'].value_counts().plot(kind='bar')
plt.title('Speed_limit')
plt.show()
