# GRÁFICO CALOR. Este quizás no cambiar el formato
pivot_table = df.pivot_table(index='Hour', columns='Day_of_Week', aggfunc='size', fill_value=0)
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_table, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Número de accidentes'})
plt.xlabel('Día de la semana', fontsize=14)
plt.ylabel('Hora del día', fontsize=14)
plt.title('Frecuencia de accidentes por hora y día de la semana', fontsize=16)
plt.show()



# FRECUENCIA DE PHYSICAL FACILITIES
frecuencia_crossing = df['Pedestrian_Crossing-Physical_Facilities'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(range(len(frecuencia_crossing)), frecuencia_crossing.values, color='darkseagreen', edgecolor='black')

plt.xticks(range(len(frecuencia_crossing)), frecuencia_crossing.index, rotation=45, ha='right')
plt.xlabel('Tipo de cruce peatonal', fontsize=14)
plt.ylabel('Frecuencia absoluta', fontsize=14)
plt.title('Frecuencia de los tipos de cruces peatonales en el lugar del accidente', fontsize=16)

plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))




# GRÁFICO CALOR DE PHYSICAL FACILITIES
crossing_severity_table = pd.crosstab(df['Pedestrian_Crossing-Physical_Facilities'], df['Accident_Severity'])

plt.figure(figsize=(12, 8))
sns.heatmap(crossing_severity_table, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Frecuencia absoluta'})

plt.xlabel('Gravedad del Accidente', fontsize=14)
plt.ylabel('Tipo de cruce peatonal', fontsize=14)
plt.title('Relación entre los tipos de cruces peatonales y la gravedad del accidente', fontsize=16)




# HISTOGRAMA CONDICIONES VÍA
plt.hist(df['Road_Surface_Conditions'], color='darkseagreen', edgecolor='black')

plt.xlabel('Condiciones de la vía', fontsize=14)
plt.ylabel('Número de accidentes', fontsize=14)
plt.title('Número de accidentes según la condición de la vía', fontsize=20)
