#Importamos todas las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

#Leemos nuestro dataframe e imprimimos para tener una primera toma de contacto
df = pd.read_csv('Accidents.csv')
df.head(10)
df.shape

#Creamos las variables categóricas
lista_cat = ['Special_Conditions_at_Site', 'Pedestrian_Crossing-Physical_Facilities','Light_Conditions',
             'Junction_Control','Road_Type','Carriageway_Hazards','Road_Surface_Conditions',
             'Pedestrian_Crossing-Human_Control', 'Weather_Conditions', 'Did_Police_Officer_Attend_Scene_of_Accident']
df[lista_cat] = df[lista_cat].astype('category')
df.dtypes

#Matriz de correlación sin las variables categóricas
df_corr = df.drop(['Date', 'Special_Conditions_at_Site', 'Pedestrian_Crossing-Physical_Facilities','Light_Conditions',
             'Junction_Control','Road_Type','Carriageway_Hazards','Road_Surface_Conditions',
             'Pedestrian_Crossing-Human_Control', 'Weather_Conditions', 'Did_Police_Officer_Attend_Scene_of_Accident'], axis=1)
correlation_matrix = df_corr.corr()
