import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import geemap.eefolium as geemap
import os
from typing import Tuple
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import geopandas as gpd
from geopandas import GeoDataFrame
import psycopg2
import plotly.figure_factory as ff
import mercantile
import folium
import streamlit as st
from streamlit_folium import folium_static
import geemap.eefolium as geemap
import ee
import time
from cachetools import cached

# service_account = 'mapswipe@test-333723.iam.gserviceaccount.com'
# credentials = ee.ServiceAccountCredentials(service_account, 'project/test-333723-8c5ebc1338a3.json')
# ee.Authenticate()
# ee.Initialize()

st.set_page_config(layout="wide", page_title="ARC MapSwipe data analysis")
st.header('Project')

@st.experimental_memo(suppress_st_warning=True)
def get_project_reviews() -> Tuple:
    with st.spinner('Loading projet data...'):
        url='https://apps.mapswipe.org/api/projects/projects.csv'
        projects_df=pd.read_csv(url)
        projects = projects_df['name'].to_list()
        arc_projects = []

        for project in projects:
            if 'American' in project and 'OSM Building Validation' in project:
                arc_projects.append(project)
        arc_df= projects_df[projects_df['name'].isin(arc_projects)]
    return projects_df, arc_df, arc_projects
        
projects_df, arc_df, arc_projects = get_project_reviews()

option = st.selectbox(
    'Select project',
    options= arc_projects)

s_project = arc_df[arc_df['name'] == option]

with st.sidebar:
    st.write(f"Project name: \n") 
    st.write(f'{option}')
    st.write(f"Project id(s): {(','.join(s_project['name'].to_list()))}")



# st.write('You selected:', option)

# table_dict = {

# 'Dar Es Salaam': 'dar_es_salaam'
# ,'Ushirombo': 'ushirombo'
# ,'Harare': 'harare'

# } 

# @st.cache(allow_output_mutation=True)
# def get_connection():
#     return sqlalchemy.create_engine('postgresql://docker:docker@db:5432/mapswipe')

# @st.experimental_memo(suppress_st_warning=True)
# def load_data(project:str) -> Tuple[gpd.GeoDataFrame,gpd.GeoDataFrame]:
    
#     with st.spinner('Loading Data...'):
#         time.sleep(0.5)
#         aoi_sql = f"SELECT ST_Force2d(wkb_geometry) AS wkb_geometry FROM {table_dict[project]}_aoi"   
#         sql = f"SELECT *  FROM {table_dict[project]}"

#         with get_connection().connect() as conn:
#             gdf_aoi = gpd.GeoDataFrame.from_postgis(aoi_sql, conn, geom_col='wkb_geometry')
#             gdf = gpd.GeoDataFrame.from_postgis(sql, conn, geom_col='wkb_geometry')
#             conn.close()

#     return gdf, gdf_aoi

# fc, aoi =  load_data(option)

# centroid = aoi.geometry.centroid
# #bbox = geemap.geopandas_to_ee(aoi)


# st.header('Extent')

# with st.echo():

#     token = 'pk.eyJ1IjoiaXNrYW5kYXJibHVlIiwiYSI6ImNpazE3MTJldjAzYzZ1Nm0wdXZnMGU2MGMifQ.i3E1_b9QXJS8xXuPy3OTcg'  # your mapbox token
#     tileurl = 'https://api.mapbox.com/v4/mapbox.satellite/{z}/{x}/{y}@2x.png?access_token=' + str(token)

#     m = folium.Map(location=[centroid[0].y, centroid[0].x], zoom_start=9, tiles=tileurl, attr='Mapbox')

#     # m = geemap.Map(center=[centroid[0].y, centroid[0].x], zoom=11)
#     #m.add_basemap('SATELLITE')
#     # m.addLayer(bbox)s
#     # m.addLayerControl()

#     # call to render Folium map in Streamlit
#     geo_j = bbox.to_json()
#     geo_j = folium.GeoJson(data=geo_j,
#                         style_function=lambda x: {'fillColor': 'orange'})
#     geo_j.add_to(m)
#     folium_static(m)

# st.header('Summary statistics')

# st.text(f'{option} project has {fc.shape[0]} buildings')

# hist_data = [fc['agreement']]
# group_labels = ['agreement']
# fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
# fig.update_xaxes(range=[0, 1])
# fig.update_yaxes(showgrid=False)
# st.plotly_chart(fig, use_container_width=True)


# selected_range = st.slider(
#      'Select a range of agreement score values', 0.0, 1.0, (0.2, 0.3))

# st.write('Values:', selected_range)

# @st.cache
# def return_subset(values: Tuple, fc: gpd.GeoDataFrame):
#     subset = fc[fc['agreement'].between(values[0], values[1])]
#     subset.reset_index(inplace=True, drop=True)
#     return subset

# subset = return_subset(values=selected_range, fc=fc)
# st.write(subset.shape[0],  'buildings within this range of agreement values')



# #create a dict with OGC FID and agreement scores

# ogc_dict = dict(zip(subset.ogc_fid, subset.agreement))

# def format_func(option):
#     return ogc_dict[option]
    
# selected_fid = st.selectbox('Select feature OGC_FID', options=list(ogc_dict.keys()))
# st.write(f"You selected option {selected_fid} with agreement score: {format_func(selected_fid)}")


# selection = subset[subset['ogc_fid'] == selected_fid]
# #selection = subset.loc[[1]]
# selection = selection[['wkb_geometry']]
# centroid = selection.geometry.centroid

# st.write(centroid.iloc[0].x)

# #feature = geemap.geopandas_to_ee(selection)

# style = {
#     'color': '#00FFFF',
#     'width': 2,
#     'lineType': 'solid',
#     'fillColor': '00000000',
# }

# #n = geemap.Map(center=[centroid.iloc[0].y, centroid.iloc[0].x], zoom=24)

# n = folium.Map(location=[centroid.iloc[0].y,centroid.iloc[0].x], zoom_start=20, max_zoom = 24, tiles=tileurl, attr='Mapbox')
# geo_j = selection.to_json()
# geo_j = folium.GeoJson(data=geo_j,
#                         style_function=lambda x: {'fillColor': 'orange'})
# geo_j.add_to(n)
# #n.add_basemap('SATELLITE')
# #n.addLayer(feature.style(**style), {}, "Styled vector")

# folium_static(n)




