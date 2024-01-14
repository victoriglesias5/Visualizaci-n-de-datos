#Importamos todas las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime

df = pd.read_csv('Accidents2.csv')

##TALIA
#%% GRÁFICO CALOR. Este quizás no cambiar el formato
pivot_table = df.pivot_table(index='Hour', columns='Day_of_Week', aggfunc='size', fill_value=0)
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_table, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Número de accidentes'})
plt.xlabel('Día de la semana', fontsize=14)
plt.ylabel('Hora del día', fontsize=14)
plt.title('Frecuencia de accidentes por hora y día de la semana', fontsize=16)
plt.show()



#%% FRECUENCIA DE PHYSICAL FACILITIES
frecuencia_crossing = df['Pedestrian_Crossing-Physical_Facilities'].value_counts()
plt.figure(figsize=(14, 8))
plt.bar(range(len(frecuencia_crossing)), frecuencia_crossing.values, color='#8B0000', edgecolor='black')

plt.yticks(fontweight='bold')
plt.xticks(range(len(frecuencia_crossing)), frecuencia_crossing.index, rotation=45, ha='right', fontweight='bold')
plt.xlabel('Tipo de cruce peatonal', fontsize=14, fontweight='bold')
plt.ylabel('Número de accidentes', fontsize=14, fontweight='bold')
plt.title('Frecuencia de los tipos de cruces peatonales en el lugar del accidente', fontsize=20, fontweight='bold')

plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))




#%% GRÁFICO CALOR DE PHYSICAL FACILITIES
crossing_severity_table = pd.crosstab(df['Pedestrian_Crossing-Physical_Facilities'], df['Accident_Severity'])

plt.figure(figsize=(14, 8))
sns.heatmap(crossing_severity_table, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Frecuencia absoluta'})

plt.xlabel('Gravedad del Accidente', fontsize=14)
plt.ylabel('Tipo de cruce peatonal', fontsize=14)
plt.title('Relación entre los tipos de cruces peatonales y la gravedad del accidente', fontsize=16)




#%% HISTOGRAMA CONDICIONES VÍA
df['Road_Surface_Conditions']=df['Road_Surface_Conditions'].replace('Flood (Over 3cm of water)','Flood (Over 3cm)')
plt.figure(figsize=(14, 8))
plt.hist(df['Road_Surface_Conditions'], color='#8B0000', edgecolor='black')

plt.yticks(fontweight='bold')
plt.xticks(fontweight='bold')
plt.ticklabel_format(axis='y', style='plain')
plt.xlabel('Condiciones de la vía', fontsize=14, fontweight='bold')
plt.ylabel('Número de accidentes', fontsize=14, fontweight='bold')
plt.title('Número de accidentes según la condición de la vía', fontsize=20, fontweight='bold')

##PEPE
#%%
crossing_severity_table = pd.crosstab(df['Road_Surface_Conditions'], 

                                      df['Accident_Severity'])
 
crossing_severity_table_percentage = crossing_severity_table.div(crossing_severity_table.sum(axis=0), axis=1) * 100
 
# Crear el heatmap con porcentajes

plt.figure(figsize=(14, 8))
sns.heatmap(crossing_severity_table_percentage, cmap='viridis', annot=True, fmt=".2f", cbar_kws={'label': 'Porcentaje'})
plt.xlabel('Accident Severity')
plt.ylabel('Road_Surface_Conditions')
plt.title('Cross-tabulation: Junction Control vs Accident Severity', fontsize = 20)
value_counts = df['Special_Conditions_at_Site'].value_counts()
bars = plt.bar(value_counts.index, value_counts.values)
plt.xlabel("Condiciones Especiales", fontsize = 14, fontweight = 'bold')
plt.xticks (rotation = 90, fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.ylabel("Numero de accidentes", fontsize = 14, fontweight = 'bold')
plt.show()

#%% plot bar por años

value_counts = df["Year"].value_counts()
plt.figure(figsize=(14, 8))
bars = plt.bar(value_counts.index, value_counts.values, color='#8B0000', edgecolor='black')
plt.xlabel("Año", fontweight = 'bold', fontsize = 14)
plt.ylabel("Número de accidentes", fontweight = 'bold', fontsize = 14)
plt.title("Accidentes por año", fontsize = 20, fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.xticks(fontweight = 'bold')
plt.show()

#%%plot bar light conditions. La mayoría de accidentes ocurren cuando existe claridad de luz, no existe una relación entre uno y otro
value_counts = df["Light_Conditions"].value_counts()
plt.figure(figsize=(14, 8))
bars = plt.bar(value_counts.index, value_counts.values, color = '#8B0000')
plt.xlabel("Condiciones Luminosas", fontsize = 14, fontweight = 'bold')
plt.xticks (rotation = 45, fontweight = 'bold', ha='right')
plt.yticks(fontweight = 'bold')
plt.ticklabel_format(axis='y', style='plain')
plt.ylabel("Numero de accidentes", fontsize = 14, fontweight = 'bold')
plt.title("Luminosidad en los accidentes", fontsize = 20, fontweight = 'bold')
plt.show()
 
# #plot bar accident severity. Aquí, fatal es 1, serious es 2 y 3 sin mayores consecuencias
# value_counts = df["Accident_Severity"].value_counts()
# pies = plt.pie(x= value_counts.values, labels = value_counts.index, autopct='%2.2f%%')
# #plt.legend(zip(value_counts.index, value_counts.values), title='Category Counts', loc='upper left', bbox_to_anchor=(1, 0.5))
# plt.show()

#%%comparación de accident severity con speed limit
sns.violinplot(x=df['Accident_Severity'], y=df['Speed_limit'])
plt.show()

#%%

##JESÚS

#%%
#La primera de las variables con la que vamos a trabajar es Carriageway_Hazards. Al hablar de peligros en la via, vamos a ver los distintos peligros, la relación con la gravedad, con el speed-limit, number of casualties
Peligros = df['Carriageway_Hazards']
plt.figure(figsize=(14, 8))
sns.countplot(x=Peligros, color='#8B0000')
plt.title('Frecuencia de Carriageway Hazards', fontsize=20, fontweight='bold')
plt.xlabel('Carriageway Hazards', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.ylabel('Frecuencia', fontweight = 'bold', fontsize = 14)
plt.show()

#%%vamos a relacionar los peligros de la vía con el speed_limit
Peligros_Grave = df.groupby(['Carriageway_Hazards', 'Speed_limit']).size().reset_index(name='count')
# Pivota la tabla para tener 'Accident_Severity' como columnas
pivot_data = Peligros_Grave.pivot(index='Carriageway_Hazards', columns='Speed_limit', values='count').fillna(0)
# Grafica el resultado
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_data, annot=True, fmt='g')
plt.title('Número de accidentes por velocidad y tipo de peligro en la vía', fontsize = 20, fontweight='bold')
plt.xlabel('Speed_Limit', fontsize = 14, fontweight='bold')
plt.ylabel('Carriageway Hazards', fontsize = 14, fontweight='bold')
plt.xticks(fontweight = 'bold')
plt.yticks(fontweight = 'bold')
plt.show()

#%%Vamos a relacionar el number of casualties con los peligros:
grouped_data = df.groupby('Carriageway_Hazards')['Number_of_Casualties'].sum().reset_index()
# Ordena los datos por el número de víctimas de forma descendente
sorted_data = grouped_data.sort_values(by='Number_of_Casualties', ascending=False)
# Grafica el resultado
plt.figure(figsize=(14, 8))
sns.barplot(x='Carriageway_Hazards', y='Number_of_Casualties', data=sorted_data, color='#8B0000')
plt.title('Relación entre Carriageway y Number of casualties', fontsize = 20, fontweight = 'bold')
plt.xlabel('Carriageway', fontsize = 14, fontweight = 'bold')
plt.ylabel('Number of casualties', fontsize = 14, fontweight = 'bold')
plt.xticks(rotation=45, ha='right', fontweight = 'bold')  # Rotar las etiquetas del eje x para mayor legibilidad
plt.yticks(fontweight = 'bold')
plt.show()

#%%Por último, vamos a analizar la variable Junction_Control
junction_control_counts = df['Junction_Control'].value_counts()
# Crear el gráfico de barras
plt.figure(figsize=(14, 8))
junction_control_counts.plot(kind='bar', color='#8B0000')
# Configurar título y etiquetas
plt.title('Distribución de Junction Control', fontweight = 'bold', fontsize = 20)
plt.xlabel('Junction Control', fontweight = 'bold', fontsize = 14)
plt.ylabel('Número de Accidentes', fontweight = 'bold', fontsize = 14)
# Mostrar los valores absolutos en las barras
for i, value in enumerate(junction_control_counts):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontweight = 'bold')
plt.xticks(rotation=45, ha='right', fontweight = 'bold')  # Rotar las etiquetas del eje x para mayor legibilidad
plt.yticks(fontweight = 'bold')
# Mostrar el gráfico de barras
plt.show()

#%%Vamos a ver los valores de la atención Policial
Atencion_Policial = df['Did_Police_Officer_Attend_Scene_of_Accident'].value_counts()
#Proporción de Atención Policial en Accidentes:
#- Yes: 81.03%
#- No: 18.97%
