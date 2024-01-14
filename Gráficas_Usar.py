#La primera de las variables con la que vamos a trabajar es Carriageway_Hazards. Al hablar de peligros en la via, vamos a ver los distintos peligros, la relación con la gravedad, con el speed-limit, number of casualties
Peligros = df['Carriageway_Hazards']
plt.figure(figsize=(10, 6))
sns.countplot(x=Peligros, palette='viridis')
plt.title('Frecuencia de Carriageway Hazards')
plt.xlabel('Carriageway Hazards')
plt.xticks(rotation=45)
plt.ylabel('Frecuencia')
plt.show()

#vamos a relacionar los peligros de la vía con el speed_limit
Peligros_Grave = df.groupby(['Carriageway_Hazards', 'Speed_limit']).size().reset_index(name='count')
# Pivota la tabla para tener 'Accident_Severity' como columnas
pivot_data = Peligros_Grave.pivot(index='Carriageway_Hazards', columns='Speed_limit', values='count').fillna(0)
# Grafica el resultado
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_data, annot=True, fmt='g')
plt.title('Número de accidentes por velocidad y tipo de peligro en la vía')
plt.xlabel('Speed_Limit')
plt.ylabel('Carriageway Hazards')
plt.show()

#Vamos a relacionar el number of casualties con los peligros:
grouped_data = df.groupby('Carriageway_Hazards')['Number_of_Casualties'].sum().reset_index()
# Ordena los datos por el número de víctimas de forma descendente
sorted_data = grouped_data.sort_values(by='Number_of_Casualties', ascending=False)
# Grafica el resultado
plt.figure(figsize=(12, 6))
sns.barplot(x='Carriageway_Hazards', y='Number_of_Casualties', data=sorted_data)
plt.title('Relación entre Carriageway y Number of casualties')
plt.xlabel('Carriageway')
plt.ylabel('Number of casualties')
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mayor legibilidad
plt.show()

#Por último, vamos a analizar la variable Junction_Control
junction_control_counts = df['Junction_Control'].value_counts()
# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
junction_control_counts.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
# Configurar título y etiquetas
plt.title('Distribución de Junction Control')
plt.xlabel('Junction Control')
plt.ylabel('Número de Accidentes')
# Mostrar los valores absolutos en las barras
for i, value in enumerate(junction_control_counts):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
# Mostrar el gráfico de barras
plt.show()

# Vamos a ver los valores de la atención Policial
Atencion_Policial = df['Did_Police_Officer_Attend_Scene_of_Accident'].value_counts()
#Proporción de Atención Policial en Accidentes:
#- Yes: 81.03%
#- No: 18.97%
