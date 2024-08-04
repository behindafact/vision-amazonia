import streamlit as st
import pandas as pd
import plotly.express as px
import folium #Librería de mapas en Python
from streamlit_folium import st_folium #Widget de Streamlit para mostrar los mapas
from folium.plugins import MarkerCluster #Plugin para agrupar marcadores
import geopandas as gpd
import geojson

df = pd.DataFrame({
    'COMUNIDAD': ['HUESITO', 'SANTA RITA', 'NIÑAL','CARTAGENA','CAÑO COLORADO','MANACAL','BACHACO','SAN JOSÉ','CARRIZAL','LAGUNA-COLORADA','ARRECIFAL','MUERCIELAGO','CUMARAL-GUAMUCO'],
    'DEFORESTATION 2023': [21037.6, 316.22, 1631.0
,729.97
,681.35
,390.76
,2394.87
,2971.7
,568.27
,4022.64
,776.46
,775.83
,3311.60
]
})


with open("proyecto.geojson",'r', encoding='utf-8') as f:
    gj = geojson.load(f)

st.header('VISOR AMAZONIA')
dfRestaurantes= pd.read_csv('googlemaps_comida china.csv')
dfRestaurantes['review_count']=dfRestaurantes['review_count'].fillna(1)

tab2,tab4=st.tabs(['Mapa deforesacion proyecto Guainia' ,'Datos'])
with tab2:
    #df = px.data.gapminder().query("year==2007")    
    fig = px.choropleth_mapbox(data_frame=df,geojson=gj,
                               locations="COMUNIDAD",
                        color="DEFORESTATION 2023",
                        center={"lat": 3.363650, "lon": -69.091847},
                        featureidkey='properties.COMUNIDAD',
                        #hover_name="country", # column to add to hover information
                        mapbox_style="carto-positron",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        zoom=6.5,
                        width= 600,
                        height= 600)
    st.plotly_chart(fig,use_container_width=True)
    #st.dataframe(df)

with tab4:
    st.dataframe(dfRestaurantes,use_container_width=True)

