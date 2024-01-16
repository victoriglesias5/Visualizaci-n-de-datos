import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Accidents_def.csv', encoding='utf-8')

st.title("Accidentes de Coche: Causa y Consecuencia")
st.markdown('---')
st.audio("Car_crash.mp3")



st.markdown('---')
st.title("INTRO")

st.markdown('---')
# GRÁFICA 1. Nº de accidentes por año
st.title("Accidentes por año")

frecuencia_por_anio = df['Año'].value_counts().reset_index()
frecuencia_por_anio.columns = ['Año', 'Frecuencia']

fig_frecuencia_por_anio = px.bar(frecuencia_por_anio,
                                 x='Año',
                                 y='Frecuencia',
                                 labels={'Frecuencia': 'Número de Accidentes'},
                                 title='Frecuencia de Accidentes por Año',
                                 template='plotly_dark')

fig_frecuencia_por_anio.update_layout(
    xaxis=dict(title='Año', title_font=dict(size=14)),
    yaxis=dict(title='Número de Accidentes', title_font=dict(size=14)),
)

st.plotly_chart(fig_frecuencia_por_anio)




st.markdown('---')
# GRÁFICA 2. Gráfico de calor x hora y día de la semana.
pivot_table = df.pivot_table(index='Hora', columns='Día_Semana', aggfunc='size', fill_value=0)
fig = px.imshow(pivot_table, labels=dict(x="Día de la semana", y="Hora del día", color="Número de accidentes"),
                x=pivot_table.columns,
                y=pivot_table.index,
                color_continuous_scale='viridis',
                width=1000,  
                height=600,  # aquí podemos ajustar ancho y altura del gráfico
                aspect="auto",  #difuminado
                )

fig.update_layout(
    title='Frecuencia de accidentes por hora y día de la semana',
    xaxis_title='Día de la semana',
    yaxis_title='Hora del día',
    xaxis=dict(tickmode='linear', tick0=0, dtick=1),  
    yaxis=dict(tickmode='linear', tick0=0, dtick=1),  
)

fig.update_traces(hoverongaps=False, hovertemplate='Número de accidentes: %{z}')

st.plotly_chart(fig)





st.markdown('---')
st.title("I PARTE")


st.markdown('---')
# GRÁFICA 3. Nº víctimas (hasta 5), de cualquer severidad
subset_df = df[df['Numero_Afectados'] <= 5]
# Calcula la frecuencia de número de víctimas por accidente
frecuencia_victimas = subset_df['Numero_Afectados'].value_counts()

# Crea un gráfico interactivo con Plotly Express
fig = px.bar(
    frecuencia_victimas,
    x=frecuencia_victimas.index,
    y=frecuencia_victimas.values,
    color_continuous_scale='#8B0000',
    labels={'x': 'Número de víctimas', 'y': 'Frecuencia'},
    title='Número de víctimas por accidente',
    width=800,
    height=500
)
# Personaliza el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Número de víctimas')),
    yaxis=dict(title=dict(text='Frecuencia')),
)
# Muestra el gráfico con Streamlit
st.plotly_chart(fig)





st.markdown('---')
# GRÁFICA 4. Nº de víctimas en accidentes mortales (severidad 1)
st.title('Nº de víctimas en accidentes graves (severidad = 1)')
subset_df = df[df['Gravedad_Accidente'] == 1]

fig = px.histogram(subset_df,
                   x='Numero_Afectados',
                   color='Numero_Afectados',
                   labels={'Numero de afectados': 'Número de víctimas'},
                   color_discrete_sequence = ['#8B0000'],
                   template='plotly_dark')

fig.update_layout(
    xaxis=dict(title='Número de víctimas', title_font=dict(size=14)),
    yaxis=dict(title='Count', title_font=dict(size=14)),
)

fig.update_layout(legend=dict(title=dict(text='Número de Afectados'),
                              traceorder='normal',
                              tracegroupgap=0))
st.plotly_chart(fig)





st.markdown('---')
# GRÁFICA 5. Nº de vehículos en accidentes de gravedad = 1
subset_df = df[df['Gravedad_Accidente'] == 1]
frecuencia_vehiculos = subset_df['Numero_Vehiculos'].value_counts()

fig = px.bar(
    frecuencia_vehiculos,
    x=frecuencia_vehiculos.index,
    y=frecuencia_vehiculos.values,
    color_continuous_scale='#8B0000',
    labels={'x': 'Número de vehículos', 'y': 'Número de accidentes graves'},
    title='Número de vehículos involucrados en accidentes graves',
    width=800,
    height=500
)

fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Número de vehículos')),
    yaxis=dict(title=dict(text='Número de accidentes graves')),
)

st.plotly_chart(fig)




st.markdown('---')
# GRÁFICA 6. Nº accidentes según la luz
value_counts_light = df["Condiciones_Luminicas"].value_counts()
fig_3 = px.bar(x=value_counts_light.index,
             y=value_counts_light.values,
             labels=dict(x="Condiciones lumínicas", y="Número de accidentes"),
             color_continuous_scale='#8B0000',
             title='Número de accidentes según las condiciones lumínicas',
             height=500, width=800)

fig_3.update_layout(xaxis_title='Condiciones lumínicas',
                  yaxis_title='Número de accidentes')

fig_3.update_traces(hovertemplate='Número de accidentes: %{y}')

st.plotly_chart(fig_3)





st.markdown('---')
# GRÁFICA 7. Nº accidentes según tipo de carretera
frecuencia_carretera = df['Tipo_Via'].value_counts()

# Crea un gráfico interactivo de barras con Plotly Express
fig = px.bar(
    frecuencia_carretera,
    x=frecuencia_carretera.index,
    y=frecuencia_carretera.values,
    color_continuous_scale='#8B0000',
    labels={'x': 'Tipo de carretera', 'y': 'Frecuencia'},
    title='Accidentes según el tipo de carretera',
    width=800,
    height=500
)
# Personaliza el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Tipo de carretera')),
    yaxis=dict(title=dict(text='Frecuencia')),
)
# Muestra el gráfico con Streamlit
st.plotly_chart(fig)






st.markdown('---')
# GRÁFICA 8. Nº accidentes según condiciones climáticas
frecuencia_condiciones = df['Condiciones_Clima'].value_counts()

# Crea un gráfico interactivo de barras con Plotly Express
fig = px.bar(
    frecuencia_condiciones,
    x=frecuencia_condiciones.index,
    y=frecuencia_condiciones.values,
    color_continuous_scale='#8B0000',
    labels={'x': 'Condiciones ambientales', 'y': 'Frecuencia'},
    title='Accidentes dadas las condiciones ambientales',
    width=800,
    height=500
)
# Personaliza el diseño del gráfico
fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Condiciones ambientales')),
    yaxis=dict(title=dict(text='Frecuencia')),
)
# Muestra el gráfico con Streamlit
st.plotly_chart(fig)








st.markdown('---')
# GRÁFICA 9. Nº accidentes según condiciones de la vía
value_counts_road = df['Estado_via'].value_counts()

fig = px.histogram(df, x='Estado_via', color_discrete_sequence = ['#8B0000'],
                   title='Número de accidentes según el estado de la vía',
                   labels={'Estado_via': 'Estado de la vía', 'count': 'Número de accidentes'},
                   height=500, width=800)

fig.update_layout(xaxis=dict(tickmode='array', tickvals=list(value_counts_road.index),
                             ticktext=list(value_counts_road.index),
                             tickangle=90),
                  yaxis=dict(title='Número de accidentes'),
                  showlegend=False)

st.plotly_chart(fig)




st.markdown('---')
# GRÁFICA 10, relacionar con la anterior. Relación severidad - estado vía
crossing_severity_table_1 = pd.crosstab(df['Estado_via'], df['Gravedad_Accidente'])

crossing_severity_table = (crossing_severity_table_1.div(crossing_severity_table_1.sum(axis=0), axis=1) * 100)

heatmap_trace = go.Heatmap(z=crossing_severity_table.values,
                          x=crossing_severity_table.columns,
                          y=crossing_severity_table.index,
                          colorscale='viridis',
                          colorbar=dict(title='Porcentaje'))

annotation_values = [list(map(lambda x: f'{x:.2f}', row)) for row in crossing_severity_table.values]

annotations = []
for i, row in enumerate(crossing_severity_table.index):
    for j, col in enumerate(crossing_severity_table.columns):
        annotations.append(
            dict(x=col, y=row, text=str(annotation_values[i][j]),
                 xref="x1", yref="y1",
                 showarrow=False, font=dict(color='white')))

layout = dict(title='Relación entre Severidad del Accidente y Estado de la vía',
              xaxis=dict(title='Severidad del Accidente', tickvals=[1, 2, 3], ticktext=['1', '2', '3']),
              yaxis=dict(title='Estado de la Vía'))

fig_5 = go.Figure(data=[heatmap_trace], layout=layout)

fig_5.update_layout(annotations=annotations)

st.plotly_chart(fig_5)




st.markdown('---')
# GRÁFICA 11. Histograma de la frecuencia de obstáculos
st.title('Frecuencia de obstáculos')
Peligros = df['Obstaculos']

fig_3 = px.histogram(df, x=Peligros, color_discrete_sequence=['#8B0000'])

fig_3.update_layout(
    xaxis=dict(title='Tipos de obstáculos', tickangle=45, title_font=dict(size=14, )),
    yaxis=dict(title='Frecuencia', title_font=dict(size=14, ), tickfont=dict(size=14, )),
    legend_title=dict(text='Obstáculos', font=dict(size=14, )),
)

st.plotly_chart(fig_3)




st.markdown('---')
# GRÁFICA 12. Obstáculos - nº de afectados
st.title('Relación entre los obstáculos y afectados en el siniestro')
grouped_data = df.groupby('Obstaculos')['Numero_Afectados'].sum().reset_index()
sorted_data = grouped_data.sort_values(by='Numero_Afectados', ascending=False)
fig_cas_peligros = px.bar(sorted_data, 
                          x='Obstaculos', 
                          y='Numero_Afectados',
                          labels={'Numero_Afectados': 'Número de Víctimas'},
                          color_continuous_scale='#8B0000',
                          template='plotly_dark')
# Personalizar el diseño del gráfico
fig_cas_peligros.update_layout(
    xaxis=dict(title='Obstáculos', tickangle=45, title_font=dict(size=14)),
    yaxis=dict(title='Número de Afectados', title_font=dict(size=14)),
)
# Mostrar el gráfico interactivo en Streamlit
st.plotly_chart(fig_cas_peligros)



st.markdown('---')
# PODRÍAMOS METER GRÁFICA ADICIONAL DE JESÚS AQUÍ: mapa de calor obstáculos-velocidad



st.markdown('---')
# GRÁFICA 13. Violín (severidad - velocidad)
fig_4 = go.Figure()

for gravity, data in df.groupby('Gravedad_Accidente'):
    fig_4.add_trace(go.Violin(x=data['Gravedad_Accidente'],
                            y=data['Speed_limit'],
                            name=gravity,
                            box_visible=True,
                            line_color='#8B0000'))

fig_4.update_layout(title='Relación entre la gravedad del accidente y la velocidad límite',
                  xaxis_title='Gravedad del Accidente',
                  yaxis_title='Límite de velocidad',
                  height=500, width=800)

st.plotly_chart(fig_4)






st.markdown('---')
st.title("II PARTE")


st.markdown('---')
# GRÁFICA 14. Histograma controles de cruce (NO HUMANOS!!!)
st.title('Frecuencia de Controles de Cruce')
junction_control_counts = df['Control_Cruce'].value_counts().reset_index()
fig_junc_cont = px.histogram(df, 
                              x='Control_Cruce', 
                              color_discrete_sequence = ['#8B0000'],
                              labels={'Control_Cruce': 'Número de Accidentes'},
                              template='plotly_dark')

fig_junc_cont.update_layout(
    xaxis=dict(title='Control de Cruce', tickangle=45, title_font=dict(size=14)),
    yaxis=dict(title='Frecuencia', title_font=dict(size=14), tickfont=dict(size=14)),
    legend_title=dict(text='Control de Cruce', font=dict(size=14)),
)

st.plotly_chart(fig_junc_cont)





st.markdown('---')
# PODRÍAMOS METER GRÁFICA ADICIONAL AQUÍ: mapa de calor que relaciona junction control - severidad (está en el doc de teams)






st.markdown('---')
# GRÁFICA 15. Condiciones especiales
 
value_counts_conditions = df['Condiciones_Especiales'].value_counts()
fig_2 = px.bar(x=value_counts_conditions.index,
             y=value_counts_conditions.values,
             labels=dict(x="Condiciones especiales", y="Número de Accidentes"),
             color_continuous_scale='#8B0000',
             title='Número de Accidentes bajo condiciones especiales',
             height=500, width=800)

fig_2.update_layout(xaxis_title='Condiciones especiales',
                  yaxis_title='Número de Accidentes')

fig_2.update_traces(hovertemplate='Número de Accidentes: %{y}')

st.plotly_chart(fig_2)






st.markdown('---')
# GRÁFICA 16. Tipos de cruces peatonales
frecuencia_crossing = df['Facilidades_Pasos'].value_counts()

fig = px.bar(frecuencia_crossing, 
             x=frecuencia_crossing.index, 
             y=frecuencia_crossing.values,
             color_continuous_scale='#8B0000',
             labels={'x': 'Tipo de cruce peatonal', 'y': 'Número de accidentes'},
             title='Frecuencia de los tipos de cruces peatonales en el lugar del accidente',
             width=800,
             height=500
             )

fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Tipo de cruce peatonal')),
    yaxis=dict(title=dict(text='Número de accidentes')),
)

st.plotly_chart(fig)



st.markdown('---')
# GRÁFICA 17. Relación tipos de cruces - gravedad accidente
pivot_table = pd.crosstab(df['Facilidades_Pasos'], df['Gravedad_Accidente'])
heatmap_trace = go.Heatmap(z=pivot_table.values,
                          x=pivot_table.columns,
                          y=pivot_table.index,
                          colorscale='viridis',
                          colorbar=dict(title='Porcentaje'))

annotation_values = [list(map(str, row)) for row in pivot_table.values]

annotations = []
for i, row in enumerate(pivot_table.index):
    for j, col in enumerate(pivot_table.columns):
        annotations.append(
            dict(x=col, y=row, text=str(annotation_values[i][j]),
                 xref="x1", yref="y1",
                 showarrow=False, font=dict(color='white')))

layout = dict(title='Severidad del accidente vs Facilidad de Pasos',
              xaxis=dict(title='Severidad del Accidente', tickvals=[1,2,3], ticktext=['1', '2', '3']),
              yaxis=dict(title='Facilidad de Pasos'))

fig_5 = go.Figure(data=[heatmap_trace], layout=layout)

fig_5.update_layout(annotations=annotations)

st.plotly_chart(fig_5)


