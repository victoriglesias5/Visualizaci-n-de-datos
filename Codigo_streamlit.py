import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Accidents_def.csv', encoding='utf-8')

# Establece el tema de Streamlit
st.set_page_config(page_title="Accidentes de Coche", page_icon="🚗", layout="wide")

# Cambia el color de fondo
st.markdown(
    """
    <style>
        body {
            background-color: #FFB6C1;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Navegación lateral
page = st.sidebar.selectbox("Seleccionar Apartado", ["Portada","Introducción", "Primera Parte", "Segunda Parte", "Conclusiones"])


if page == "Portada":
    st.markdown("""
        <h1 style='text-align: center; color: #8B0000; font-family: "Helvetica Neue",Helvetica,Arial,sans-serif; font-size: 36px;'>
            Accidentes de Coche: Causa y Consecuencia
        </h1>
    """, unsafe_allow_html=True)
    
    # Portada con imagen
    st.image("Foto.jpg", use_column_width=True)
    st.audio("Car_Crash.mp3")
    

if page == "Introducción":

    st.markdown("<h2 style='text-align: center;'>INTRODUCCIÓN</h2>", unsafe_allow_html=True)

    st.markdown('---')
 
    # GRÁFICA 1. Nº de accidentes por año
    frecuencia_por_anio = df['Año'].value_counts().reset_index().sort_values(by="Año")
    frecuencia_por_anio.columns = ['Año', 'Frecuencia']
    
    fig_frecuencia_por_anio = px.line(frecuencia_por_anio,
                                     x='Año',
                                     y='Frecuencia',
                                     title='Número de accidentes por año',
                                     color_discrete_sequence = ["#8B0000"],
                                     markers=True)
    
    fig_frecuencia_por_anio.update_layout(
        xaxis=dict(title='Año', title_font=dict(size=14)),
        yaxis=dict(title='Número de accidentes', title_font=dict(size=14)),
    )
    
    st.plotly_chart(fig_frecuencia_por_anio)
    
    
    
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
        title='Número de accidentes por hora y día de la semana',
        xaxis_title='Día de la semana',
        yaxis_title='Hora del día',
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),  
        yaxis=dict(tickmode='linear', tick0=0, dtick=1),  
    )
    
    fig.update_traces(hoverongaps=False, hovertemplate='Número de accidentes: %{z}')
    
    st.plotly_chart(fig)
    
    
    
    
    
    st.markdown('---')

elif page == "Primera Parte":

    st.markdown("<h2 style='text-align: center;'>PRIMERA PARTE</h2>", unsafe_allow_html=True)


    st.markdown('---')

    # GRÁFICA 3. Nº de vehículos 
    frecuencia_vehiculos = df['Numero_Vehiculos'].value_counts()
    
    fig_1 = px.bar(
        frecuencia_vehiculos,
        x=frecuencia_vehiculos.index,
        y=frecuencia_vehiculos.values,
        color_discrete_sequence=['#8B0000'],
        title='Número de vehículos por accidente',
        width=800,
        height=500
    )
    
    fig_1.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1, title=dict(text='Número de vehículos')),
        yaxis=dict(title=dict(text='Número de accidentes')),
    )
    
    st.plotly_chart(fig_1)

    
    
    # GRÁFICA 4. Nº víctimas
    
    frecuencia_victimas = df['Numero_Afectados'].value_counts()
    
    fig_2 = px.bar(
        frecuencia_victimas,
        x=frecuencia_victimas.index,
        y=frecuencia_victimas.values,
        color_discrete_sequence=['#8B0000'],
        title='Número de víctimas por accidente',
        width=1200,
        height=500
    )
    
    fig_2.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1, title=dict(text='Número de víctimas')),
        yaxis=dict(title=dict(text='Número de accidentes')),
    )
    
    st.plotly_chart(fig_2)
 
    
    # GRÁFICA 5. Nº accidentes según la luz
    value_counts_light = df["Condiciones_Luminicas"].value_counts()
    fig_3 = px.bar(x=value_counts_light.index,
                 y=value_counts_light.values,
                 labels=dict(x="Condiciones lumínicas", y="Número de accidentes"),
                 color_discrete_sequence=['#8B0000'],
                 title='Número de accidentes según las condiciones lumínicas',
                 height=500, width=800)
    
    fig_3.update_layout(xaxis_title='Condiciones lumínicas',
                      yaxis_title='Número de accidentes')
    
    fig_3.update_traces(hovertemplate='Número de accidentes: %{y}')
    
    st.plotly_chart(fig_3)
    
    
    
    
    # GRÁFICA 6. Nº accidentes según tipo de carretera
    frecuencia_carretera = df['Tipo_Via'].value_counts()
    
    fig_4 = px.bar(
        frecuencia_carretera,
        x=frecuencia_carretera.index,
        y=frecuencia_carretera.values,
        color_discrete_sequence=['#8B0000'],
        labels={'x': 'Tipo de carretera', 'y': 'Número de accidentes'},
        title='Número de accidentes según el tipo de carretera',
        width=800,
        height=500
    )
    
    fig_4.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Tipo de carretera')),
        yaxis=dict(title=dict(text='Número de accidentes')),
    )
    
    st.plotly_chart(fig_4)
    
    
        # GRÁFICA 7. Obstáculos
    value_counts_obstacles = df['Obstaculos'].value_counts()

    fig_5 = px.bar(
        value_counts_obstacles,
        x=value_counts_obstacles.index,
        y=value_counts_obstacles.values,
        color_discrete_sequence=['#8B0000'],
        width=800,
        height=500
    )
    
    fig_5.update_layout(title='Número de accidentes provocados por obstáculos',
        xaxis=dict(title='Tipos de obstáculos', tickangle=45, title_font=dict(size=14, )),
        yaxis=dict(title='Número de accidentes', title_font=dict(size=14, ), tickfont=dict(size=14, )))
    
    st.plotly_chart(fig_5)  
    
    
    # GRÁFICA 8. Nº accidentes según condiciones climáticas
    frecuencia_condiciones = df['Condiciones_Clima'].value_counts()
    
    fig_6 = px.bar(
        frecuencia_condiciones,
        x=frecuencia_condiciones.index,
        y=frecuencia_condiciones.values,
        color_discrete_sequence=['#8B0000'],
        labels={'x': 'Condiciones climatológicas', 'y': 'Número de accidentes'},
        title='Número de accidentes dadas las condiciones climatológicas',
        width=800,
        height=500
    )
    
    fig_6.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='Condiciones climatológicas')),
        yaxis=dict(title=dict(text='Número de accidentes')),
    )
    
    st.plotly_chart(fig_6)
    
    
    
    
    
    
    # GRÁFICA 9. Nº accidentes según condiciones de la vía
    value_counts_road = df['Estado_via'].value_counts()
    
    fig_7 = px.bar(
        value_counts_road,
        x=value_counts_road.index,
        y=value_counts_road.values,
        color_discrete_sequence=['#8B0000'],
        title='Número de accidentes según las condiciones de la vía',
        width=800,
        height=500
    )
    
    fig_7.update_layout(xaxis=dict(title='Condiciones de la vía', tickmode='array', tickvals=list(value_counts_road.index),
                                 ticktext=list(value_counts_road.index),
                                 tickangle=45),
                      yaxis=dict(title='Número de accidentes'),
                      showlegend=False)
    
    st.plotly_chart(fig_7)
    
    
    
    
    # GRÁFICA 10. Relación gravedad - estado vía
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
    
    layout = dict(title='Relación entre la gravedad del accidente y las condiciones de la vía',
                  xaxis=dict(title='Gravedad del Accidente', tickvals=[1, 2, 3], ticktext=['1', '2', '3']),
                  yaxis=dict(title='Condiciones de la Vía'))
    
    fig_8 = go.Figure(data=[heatmap_trace], layout=layout)
    
    fig_8.update_layout(annotations=annotations)

    st.plotly_chart(fig_8)


    
    
    # GRÁFICA 11. Condiciones especiales
     
    value_counts_conditions = df['Condiciones_Especiales'].value_counts()
    fig_9 = px.bar(x=value_counts_conditions.index,
                 y=value_counts_conditions.values,
                 labels=dict(x="Condiciones especiales", y="Número de Accidentes"),
                 color_discrete_sequence=['#8B0000'],
                 title='Número de accidentes provocados por condiciones especiales',
                 height=500, width=800)
    
    fig_9.update_layout(xaxis_title='Condiciones especiales',
                      yaxis_title='Número de accidentes')
    
    fig_9.update_traces(hovertemplate='Número de Accidentes: %{y}')
    
    st.plotly_chart(fig_9) 
    


    # GRÁFICA 12. Violín (severidad - velocidad)
    fig_10 = go.Figure()
    
    for gravity, data in df.groupby('Gravedad_Accidente'):
        fig_10.add_trace(go.Violin(x=data['Gravedad_Accidente'],
                                y=data['Speed_limit'],
                                name=gravity,
                                box_visible=True,
                                line_color='#8B0000',
                                showlegend=False))
    
    fig_10.update_layout(title='Relación entre la gravedad del accidente y la velocidad límite',
                      xaxis_title='Gravedad del Accidente',
                      yaxis_title='Límite de velocidad (millas/h)',
                      height=500, width=800)
    
    st.plotly_chart(fig_10)
    st.markdown('---')




elif page == "Segunda Parte":



    st.markdown('---')
    
    st.markdown("<h2 style='text-align: center;'>SEGUNDA PARTE</h2>", unsafe_allow_html=True)
    
    st.markdown('---')
    
    
    # GRÁFICA 13. Histograma controles de cruce (NO HUMANOS!!!)
    junction_control_counts = df['Control_Cruce'].value_counts()
    fig_junc_cont = px.bar(x=junction_control_counts.index,
                 y=junction_control_counts.values,
                 color_discrete_sequence=['#8B0000'],
                 height=500, width=800)
    
    fig_junc_cont.update_layout(title='Número de accidentes según los controles en los cruces',
        xaxis=dict(title='Tipo de control en el cruce', tickangle=45, title_font=dict(size=14)),
        yaxis=dict(title='Número de accidentes', title_font=dict(size=14), tickfont=dict(size=14)),
    )
    
    st.plotly_chart(fig_junc_cont)
    
    
    
    
    st.markdown('---')
    
    
    # GRÁFICA 14. Severidad - tipos de cruces 
    frecuencia_crossing = df['Facilidades_Pasos'].value_counts()
    
    fig_11 = px.bar(frecuencia_crossing, 
                 x=frecuencia_crossing.index, 
                 y=frecuencia_crossing.values,
                 color_discrete_sequence=['#8B0000'],
                 labels={'x': 'Tipo de cruce peatonal', 'y': 'Número de accidentes'},
                 title='Número de accidentes según el tipo de cruce peatonales',
                 width=800,
                 height=500
                 )
    
    fig_11.update_layout(
        xaxis=dict(tickmode='linear', tick0=0, dtick=1, tickangle=45, title=dict(text='')),
        yaxis=dict(title=dict(text='')),
    )
    
    st.plotly_chart(fig_11)
    
    
    
    
    # GRÁFICA 15. Relación tipos de cruces - gravedad accidente
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
    
    layout = dict(title='Relación entre la severidad del accidente y la existencia de cruces peatonales',
                  xaxis=dict(title='Severidad del accidente', tickvals=[1,2,3], ticktext=['1', '2', '3']),
                  yaxis=dict(title='Tipo de cruce peatonal'))
    
    fig_12 = go.Figure(data=[heatmap_trace], layout=layout)
    
    fig_12.update_layout(annotations=annotations)
    
    st.plotly_chart(fig_12)
    st.markdown('---')

    # GRÁFICA 16. Policía
    atencion_policial = df['Atencion_Policial'].value_counts()
    colors = ['#8B0000', '#00FF7F']
    # Crear un gráfico de tarta con plotly y personalizar los colores
    fig_13 = px.pie(
        names=atencion_policial.index,
        values=atencion_policial.values,
        labels=['Si', 'No'],
        title='Proporción de atención policial en accidentes',
        color_discrete_sequence=colors,
        width=700,
        height=700

    )

    # Configurar el color del texto en blanco
    fig_13.update_traces(textposition='inside', 
                         textinfo='percent+label',
                         textfont_size=30)

    st.plotly_chart(fig_13, use_container_width=True)


elif page == "Conclusiones":
    st.markdown("""
        <h1 style='text-align: center; color: #8B0000; font-family: "Helvetica Neue",Helvetica,Arial,sans-serif; font-size: 36px;'>
            CONCLUSIONES
        </h1>
    """, unsafe_allow_html=True)
    
    st.markdown('---')
    
    st.image("foto_conclusion.jpg", use_column_width=True)
