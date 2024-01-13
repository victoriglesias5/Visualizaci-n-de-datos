#Importamos todas las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

df = pd.read_csv('UK_Accident.csv')

plt.scatter(acc.Longitude,acc.Latitude,c = acc.Police_Force)

plt.scatter(acc.Longitude,acc.Latitude,c = acc.Accident_Severity)

acc_count = acc.groupby(acc.Accident_Severity).Accident_Severity.count().plot(kind = 'bar')

acc_count = acc.groupby(acc.Light_Conditions).Accident_Severity.count().plot(kind = 'bar')

acc_count = acc.groupby(acc.Road_Surface_Conditions).Accident_Severity.count().plot(kind = 'bar')

acc_count = acc.groupby(acc.Weather_Conditions).Accident_Severity.count().plot(kind = 'bar')

acc.groupby(acc.Number_of_Vehicles).Accident_Severity.count().plot(kind = 'bar')



