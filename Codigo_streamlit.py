import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Accidents_def.csv', encoding='utf-8')

st.title("Accidentes de Coche: Causa y Consecuencia")
st.markdown('---')
st.audio("Car_crash.mp3")


# TALÍA

st.markdown('---')
# GRÁFICO CALOR
pivot_table = df.pivot_table(index='Hora', columns='Día_semana', aggfunc='size', fill_value=0)
fig = px.imshow(pivot_table, 
                labels=dict(x="Día de la semana", y="Hora del día", color="Número de accidentes"),
                x=pivot_table.columns,
                y=pivot_table.index,
                color_continuous_scale='viridis',
                width=1000,  # Ajusta el ancho del gráfico según tus necesidades
                height=600,  # Ajusta la altura del gráfico según tus necesidades
                aspect="auto",  # Ajusta el aspecto del gráfico para que no se vea difuminado
                )
# Añadir información al gráfico
fig.update_layout(
    title='Frecuencia de accidentes por hora y día de la semana',
    xaxis_title='Día de la semana',
    yaxis_title='Hora del día',
    xaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Mostrar todos los ticks en el eje x
    yaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Mostrar todos los ticks en el eje y
)
# Configuración adicional para hacer el gráfico más interactivo
fig.update_traces(hoverongaps=False, hovertemplate='Número de accidentes: %{z}')
# Mostrar el gráfico con streamlit
st.plotly_chart(fig)


st.markdown('---')
# PHYSICAL FACILITIES
frecuencia_crossing = df['Facilidades_Pasos'].value_counts()
# Crear un gráfico interactivo con Plotly Express
fig = px.bar(frecuencia_crossing, 
             x=frecuencia_crossing.index, 
             y=frecuencia_crossing.values,
             color_continuous_scale='#8B0000',
             labels={'x': 'Tipo de cruce peatonal', 'y': 'Número de accidentes'},
             title='Frecuencia de los tipos de cruces peatonales en el lugar del accidente',
             width=800,
             height=500)
# Personalizar el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Tipo de cruce peatonal')),
    yaxis=dict(title=dict(text='Número de accidentes')),
)
# Mostrar el gráfico con streamlit
st.plotly_chart(fig)


st.markdown('---')
# FACILITIES - GRÁFICO CALOR
crossing_severity_table = pd.crosstab(df['Pedestrian_Crossing-Physical_Facilities'], df['Accident_Severity'])

fig, ax = plt.subplots(figsize=(14, 8))
sns.heatmap(crossing_severity_table, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Frecuencia absoluta'})

ax.set_xlabel('Gravedad del Accidente', fontsize=14)
ax.set_ylabel('Tipo de cruce peatonal', fontsize=14)
ax.set_title('Relación entre los tipos de cruces peatonales y la gravedad del accidente', fontsize=16)

st.pyplot(fig)


st.markdown('---')
# Crear un DataFrame de ejemplo
data = {'Pedestrian_Crossing-Physical_Facilities': ['Zebra Crossing', 'Traffic Signal', 'Zebra Crossing', 'Traffic Signal', 'No Physical Crossing', 'Zebra Crossing'],
        'Accident_Severity': ['Fatal', 'Serious', 'Slight', 'Fatal', 'Serious', 'Slight']}
df = pd.DataFrame(data)

# Widget interactivo para elegir el método de agregación
aggregation_method = st.selectbox('Selecciona el método de agregación:', ['count', 'sum', 'mean'])

# Realizar la agregación
crossing_severity_table = pd.crosstab(df['Pedestrian_Crossing-Physical_Facilities'], df['Accident_Severity'], margins=True, margins_name="Total")

# Configurar el tamaño del gráfico
fig, ax = plt.subplots(figsize=(14, 8))

# Crear un mapa de calor interactivo
sns.heatmap(crossing_severity_table, cmap='viridis', annot=True, fmt=f'.{0 if aggregation_method == "count" else 2}f', cbar_kws={'label': 'Frecuencia absoluta'})

# Personalizar etiquetas y título
ax.set_xlabel('Gravedad del Accidente', fontsize=14)
ax.set_ylabel('Tipo de cruce peatonal', fontsize=14)
ax.set_title('Relación entre los tipos de cruces peatonales y la gravedad del accidente', fontsize=16)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)





st.markdown('---')
# CONDICIONES VÍA
df['Road_Surface_Conditions']=df['Road_Surface_Conditions'].replace('Flood (Over 3cm of water)','Flood (Over 3cm)')
value_counts_road = df["Road_Surface_Conditions"].value_counts()
fig_5, ax = plt.subplots(figsize=(14, 8))
ax.hist(df['Road_Surface_Conditions'], color='#8B0000', edgecolor='black')
ax.set_xticklabels(value_counts_road.index,rotation = 90, fontweight = 'bold', ha='right')
ax.set_yticklabels(ax.get_yticks(), fontweight = 'bold')
#plt.ticklabel_format(axis='y', style='plain')
ax.set_xlabel('Condiciones de la vía', fontsize=14, fontweight='bold')
ax.set_ylabel('Número de accidentes', fontsize=14, fontweight='bold')
ax.set_title('Número de accidentes según la condición de la vía', fontsize=20, fontweight='bold')
st.pyplot(fig_5)





# JESÚS
st.markdown('---')
# OBSTÁCULOS
Peligros = df['Carriageway_Hazards']
st.title('Frecuencia de Carriageway Hazards')
fig_3, ax = plt.subplots(figsize=(14, 8))
sns.countplot(x=Peligros, color='#8B0000')
plt.title('Frecuencia de Carriageway Hazards', fontsize=20, fontweight='bold')
plt.xlabel('Carriageway Hazards', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontweight='bold')
plt.yticks(fontweight='bold')
plt.ylabel('Frecuencia', fontweight='bold', fontsize=14)
st.pyplot(fig_3)


st.markdown('---')
# OBSTÁCULOS - CASUALTIES
grouped_data = df.groupby('Carriageway_Hazards')['Number_of_Casualties'].sum().reset_index()
sorted_data = grouped_data.sort_values(by='Number_of_Casualties', ascending=False)
st.title('Relación entre Carriageway y Number of Casualties')
cas_peligros, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x='Carriageway_Hazards', y='Number_of_Casualties', data=sorted_data, color='#8B0000')
plt.title('Relación entre Carriageway y Number of Casualties', fontsize=20, fontweight='bold')
plt.xlabel('Carriageway', fontsize=14, fontweight='bold')
plt.ylabel('Number of Casualties', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontweight='bold')  
plt.yticks(fontweight='bold')
st.pyplot(cas_peligros)


st.markdown('---')
# JUNCTION CONTROL
st.title('Distribución de Junction Control')
junction_control_counts = df['Junction_Control'].value_counts()
Junc_cont, ax = plt.subplots(figsize=(14, 8))
ax.bar(junction_control_counts.index, junction_control_counts, color='#8B0000')
plt.title('Distribución de Junction Control', fontweight='bold', fontsize=20)
plt.xlabel('Junction Control', fontweight='bold', fontsize=14)
plt.ylabel('Número de Accidentes', fontweight='bold', fontsize=14)
for i, value in enumerate(junction_control_counts):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom', fontweight='bold')
plt.xticks(rotation=45, ha='right', fontweight='bold')  
plt.yticks(fontweight='bold')
st.pyplot(Junc_cont)



st.markdown('---')
# SEVERITY
subset_df = df[df['Accident_Severity'] == 1]
st.title('Número de víctimas graves en cada accidente')
fig, ax = plt.subplots(figsize=(14, 8))
casualties_counts = subset_df['Number_of_Casualties'].value_counts()
total_grave_accidents = sum(casualties_counts)
subset_df = df[(df['Number_of_Casualties'] <= 5) & (df['Accident_Severity'] == 1)]
num_casualties_per_severity_counts = subset_df['Number_of_Casualties'].value_counts()
sns.countplot(x='Number_of_Casualties', data=subset_df, color='#8B0000')
for i, count in enumerate(num_casualties_per_severity_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom', fontweight='bold')
plt.text(len(num_casualties_per_severity_counts) - 1, max(num_casualties_per_severity_counts) + 1,
         f'Total: {total_grave_accidents}', ha='center', va='bottom', fontweight='bold', color='red')
plt.xlabel('Número de víctimas', fontweight='bold', fontsize=14)
plt.ylabel('Count', fontweight='bold', fontsize=14)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.title('Número de víctimas graves en cada accidente', fontweight='bold', fontsize=20)
st.pyplot(fig)






# PEPE

crossing_severity_table = pd.crosstab(df['Road_Surface_Conditions'], df['Accident_Severity'])
 
crossing_severity_table_percentage = crossing_severity_table.div(crossing_severity_table.sum(axis=0), axis=1) * 100


st.markdown('---')
#
fig_1, ax = plt.subplots(figsize=(14, 8))
plot = sns.heatmap(crossing_severity_table_percentage, cmap='viridis', annot=True, fmt=".2f", cbar_kws={'label': 'Porcentaje'})
ax.set_xlabel('Accident Severity', fontsize=14)
ax.set_ylabel('Road_Surface_Conditions', fontsize=14)
ax.set_title('Cross-tabulation: Junction Control vs Accident Severity', fontsize=16)
st.pyplot(fig_1)


st.markdown('---')
#Special Conditions at site
 
value_counts_conditions = df['Special_Conditions_at_Site'].value_counts()
fig_2, ax = plt.subplots()
ax.bar(value_counts_conditions.index, value_counts_conditions.values, color='#8B0000')
ax.set_xlabel("Special Conditions", fontsize = 14, fontweight = 'bold')
ax.set_xticklabels(value_counts_conditions.index, rotation=90, fontweight='bold')
ax.set_yticklabels(ax.get_yticks(), fontweight='bold')
ax.set_ylabel("Number of Accidnets", fontsize = 14, fontweight = 'bold')
ax.set_title('Number of Accidents under Special Conditions', fontsize=16)
st.pyplot(fig_2)



#
st.markdown('---')
value_counts_light = df["Light_Conditions"].value_counts()
plt.figure(figsize=(14, 8))
fig_3, ax = plt.subplots()
ax.bar(value_counts_light.index, value_counts_light.values, color = '#8B0000')
ax.set_xlabel("Condiciones Luminosas", fontsize = 14, fontweight = 'bold')
ax.set_xticklabels(value_counts_light.index,rotation = 90, fontweight = 'bold', ha='right')
ax.set_yticklabels(ax.get_yticks(), fontweight = 'bold')
#ax.set_ticklabel_format(axis='y', style='plain')
ax.set_ylabel("Numero de accidentes", fontsize = 14, fontweight = 'bold')
ax.set_title("Luminosidad en los accidentes", fontsize = 20, fontweight = 'bold')
st.pyplot(fig_3)


#
st.markdown('---')
fig_4, ax = plt.subplots(figsize=(14, 8))
sns.violinplot(x=df['Accident_Severity'], y=df['Speed_limit'], color = '#8B0000')
st.pyplot(fig_4)




#  VICTOR

# Muertos
st.markdown('---')
subset_df = df[df['Accident_Severity'] == 1]
st.title('Número de víctimas graves en cada accidente')
fig, ax = plt.subplots(figsize=(14, 8))
casualties_counts = subset_df['Number_of_Casualties'].value_counts()
total_grave_accidents = sum(casualties_counts)
subset_df = df[(df['Number_of_Casualties'] <= 5) & (df['Accident_Severity'] == 1)]
num_casualties_per_severity_counts = subset_df['Number_of_Casualties'].value_counts()
sns.countplot(x='Number_of_Casualties', data=subset_df, color='#8B0000')
for i, count in enumerate(num_casualties_per_severity_counts):
    plt.text(i, count + 0.1, str(count), ha='center', va='bottom', fontweight='bold')
plt.text(len(num_casualties_per_severity_counts) - 1, max(num_casualties_per_severity_counts) + 1,
         f'Total: {total_grave_accidents}', ha='center', va='bottom', fontweight='bold', color='red')
plt.xlabel('Número de víctimas', fontweight='bold', fontsize=14)
plt.ylabel('Count', fontweight='bold', fontsize=14)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.title('Número de víctimas graves en cada accidente', fontweight='bold', fontsize=20)
st.pyplot(fig)


# vehículos en severidad 1
st.markdown('---')
subset_df = df[df['Accident_Severity'] == 1]
st.title('Número de vehículos involucrados en accidentes graves')
fig, ax = plt.subplots(figsize=(14, 8))
sns.countplot(x='Number_of_Vehicles', data=subset_df, color='#8B0000')
plt.title('Número de vehículos involucrados en accidentes graves', fontweight='bold', fontsize=20)
plt.xlabel('Número de vehículos', fontweight='bold', fontsize=14)
plt.ylabel('Número de accidentes graves', fontweight='bold', fontsize=14)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
st.pyplot(fig)


# victimas x accidente
st.markdown('---')
subset_df = df[df['Number_of_Casualties'] <= 5]
st.title('Número de víctimas por accidente')
fig, ax = plt.subplots(figsize=(14, 8))
sns.countplot(x='Number_of_Casualties', data=subset_df, color='#8B0000')
plt.title('Número de víctimas por accidente', fontsize=20, fontweight='bold')
plt.xlabel('Número de víctimas', fontsize=14, fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.ticklabel_format(axis='y', style='plain')
plt.ylabel('Frecuencia', fontweight='bold', fontsize=14)
st.pyplot(fig)



# accidentes - condiciones climaticas
st.markdown('---')
st.title('Accidentes respecto a las condiciones ambientales')
fig, ax = plt.subplots(figsize=(14, 8))
sns.countplot(x='Weather_Conditions', data=df, color='#8B0000')
plt.title('Accidentes respecto a las condiciones ambientales', fontsize=20, fontweight='bold')
plt.xlabel('Condiciones ambientales', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontweight='bold', ha='right')
plt.yticks(fontweight='bold')
plt.ylabel('Frecuencia', fontweight='bold', fontsize=14)
st.pyplot(fig)



# accidentes - tipo carretera
st.markdown('---')
st.title('Accidentes respecto a los tipos de carretera')
fig, ax = plt.subplots(figsize=(14, 8))
sns.countplot(x='Road_Type', data=df, color='#8B0000')
plt.title('Accidentes respecto a los tipos de carretera', fontsize=20, fontweight='bold')
plt.xlabel('Tipos de carretera', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, fontweight='bold', ha='right')
plt.yticks(fontweight='bold')
plt.ylabel('Frecuencia', fontweight='bold', fontsize=14)
st.pyplot(fig)
