# -- import modules start --
# folium
import folium

# streamlit
import streamlit as st
from streamlit_folium import st_folium
import extra_streamlit_components as stx
from streamlit_echarts import st_echarts

# requests data
import json
import requests

# data analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D
import matplotlib as mpl
import math

# customized modules
from \/Database\/database import connectDB

# -- import modules end --

# calculator distance
def calculate_distance(df, center_xy):
  df_distance = pd.DataFrame()
  distance_list = []
  for i in df['latlon']:
    if i != None or i != '':
      if type(i) == str:
        i = i[1:-1].split(', ')
        y = abs(float(center_xy[0]) - float(i[0])) * 111
        x = (math.cos(float(center_xy[0])) * 6400 * 2 * 3.14 / 360) * abs(float(center_xy[1]) - float(i[1]))
        distance = math.sqrt(x*x + y*y)
        if distance <= 3.0:
          df_distance = pd.concat([df_distance, df[df['latlon'] == ('(' + i[0] + ', ' + i[1] + ')')]])
          distance_list.append(distance)

  df_distance = df_distance.drop_duplicates()
  df_distance['distance'] = distance_list

  return df_distance

# 지도 생성
def makeMap(address):
  center_xy = list(addr_to_lat_lon(address))
  m = folium.Map(location=center_xy, zoom_start=16)
  folium.Marker(center_xy, 
                popup="회사명",
                tooltip="회사명",
                icon=(folium.Icon(color='blue', icon='building', prefix='fa'))
                ).add_to(m)
  
  df_subway = pd.read_csv('./data/subway.csv')
  df_bus = pd.read_csv('./data/bus.csv')
  df_hospital = pd.read_csv('./data/hospital.csv')
  df_museum = pd.read_csv('./data/museum.csv')
  
  df_subway_distance = calculate_distance(df_subway, center_xy)
  df_bus_distance = calculate_distance(df_bus, center_xy)
  df_hospital_distance = calculate_distance(df_hospital, center_xy)
  df_museum_distance = calculate_distance(df_museum, center_xy)

  df_subway_distance = df_subway_distance.astype({'latlon' : 'object'})
  df_bus_distance = df_bus_distance.astype({'latlon' : 'object'})
  df_hospital_distance = df_hospital_distance.astype({'latlon' : 'object'})
  df_museum_distance = df_museum_distance.astype({'latlon' : 'object'})

  df_graph = pd.DataFrame({'distance': ['500m', '1km', '3km']})

  df_graph['subway'] = [len(df_subway_distance.loc[df_subway_distance['distance'] <= 0.5]),
                    len(df_subway_distance.loc[(df_subway_distance['distance'] > 0.5) & (df_subway_distance['distance'] <= 1.0)]),
                    len(df_subway_distance.loc[(df_subway_distance['distance'] > 1.0) & (df_subway_distance['distance'] <= 3.0)])]

  df_graph['bus'] = [len(df_bus_distance.loc[df_bus_distance['distance'] <= 0.5]),
                    len(df_bus_distance.loc[(df_bus_distance['distance'] > 0.5) & (df_bus_distance['distance'] <= 1.0)]),
                    len(df_bus_distance.loc[(df_bus_distance['distance'] > 1.0) & (df_bus_distance['distance'] <= 3.0)])]

  df_graph['hospital'] = [len(df_hospital_distance.loc[df_hospital_distance['distance'] <= 0.5]),
                    len(df_hospital_distance.loc[(df_hospital_distance['distance'] > 0.5) & (df_hospital_distance['distance'] <= 1.0)]),
                    len(df_hospital_distance.loc[(df_hospital_distance['distance'] > 1.0) & (df_hospital_distance['distance'] <= 3.0)])]

  df_graph['museum'] = [len(df_museum_distance.loc[df_museum_distance['distance'] <= 0.5]),
                    len(df_museum_distance.loc[(df_museum_distance['distance'] > 0.5) & (df_museum_distance['distance'] <= 1.0)]),
                    len(df_museum_distance.loc[(df_museum_distance['distance'] > 1.0) & (df_museum_distance['distance'] <= 3.0)])]

  options = {
    "title": {"show": True, "subtext": "500m", "subtextStyle": {"align": "center", "verticalAlign": "middle"}},
    "tooltip": {"trigger": "item"},
    "legend": {"top": "0%", "left": "center"},
    "series": [
      {
        "name": "500m",
        "type": "pie",
        "radius": ["20%", "40%"],
        "avoidLabelOverlap": False,
        "itemStyle": {
          "borderRadius": 10,
          "borderColor": "#fff",
          "borderWidth": 2,
        },
        "label": {"show": False, "position": "center"},
        "emphasis": {
          "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
        },
        "labelLine": {"show": False},
        "data": [
          {"value": int(df_graph.iloc[0]['subway']), "name": "지하철역"},
          {"value": int(df_graph.iloc[0]['bus']), "name": "버스정류장"},
          {"value": int(df_graph.iloc[0]['hospital']), "name": "병원"},
          {"value": int(df_graph.iloc[0]['museum']), "name": "박물관/미술관"},
        ],
      },
      {
        "name": "1km",
        "type": "pie",
        "radius": ["40%", "60%"],
        "avoidLabelOverlap": False,
        "itemStyle": {
          "borderRadius": 15,
          "borderColor": "#fff",
          "borderWidth": 2,
        },
        "label": {"show": False, "position": "center"},
        "emphasis": {
          "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
        },
        "labelLine": {"show": False},
        "data": [
          {"value": int(df_graph.iloc[1]['subway']), "name": "지하철역"},
          {"value": int(df_graph.iloc[1]['bus']), "name": "버스정류장"},
          {"value": int(df_graph.iloc[1]['hospital']), "name": "병원"},
          {"value": int(df_graph.iloc[1]['museum']), "name": "박물관/미술관"},
        ],
      },
      {
        "name": "3km",
        "type": "pie",
        "radius": ["60%", "80%"],
        "avoidLabelOverlap": False,
        "itemStyle": {
          "borderRadius": 20,
          "borderColor": "#fff",
          "borderWidth": 2,
        },
        "label": {"show": False, "position": "center"},
        "emphasis": {
          "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
        },
        "labelLine": {"show": False},
        "data": [
          {"value": int(df_graph.iloc[2]['subway']), "name": "지하철역"},
          {"value": int(df_graph.iloc[2]['bus']), "name": "버스정류장"},
          {"value": int(df_graph.iloc[2]['hospital']), "name": "병원"},
          {"value": int(df_graph.iloc[2]['museum']), "name": "박물관/미술관"},
        ],
      }
    ],
  }
  st_echarts(
    options=options, height=500
  )
  
  makeMarker(m, df_subway_distance, 'green', 'train')
  makeMarker(m, df_bus_distance, 'green', 'bus')
  makeMarker(m, df_hospital_distance, 'red', 'plus')
  makeMarker(m, df_museum_distance, 'blue', 'landmark')
  return m

# Marker
def makeMarker(m, df, color, icon):
  for idx, row in df.iterrows():
    loc = row['latlon'][1:-1].split(', ')
    folium.Marker(loc,
                  popup=folium.Popup(row['name'], max_width=300),
                  tooltip=row['name'],
                  icon=(folium.Icon(color=color, icon=icon, prefix='fa'))
                 ).add_to(m)
    
# streamlit Router
def initRouter():
  return stx.Router({'/select': selectWork, '/map': map})

# define 직장선택
def selectWork():
  st.title('selectWork')
  if st.button('선택'):
    st.session_state.address = "부산광역시 해운대구 수영강변대로 140"
    router.route('/map')

# define 지도 탭
def map():
  address = st.session_state.address
  st.title('Map')
  m = makeMap(address)

  st_folium(m, width=725, returned_objects=[])

def addr_to_lat_lon(addr):
  url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
  headers = {"Authorization": "KakaoAK " + API_KEY}
  result = json.loads(str(requests.get(url, headers=headers).text))
  match_first = result['documents'][0]['address']
  return float(match_first['y']), float(match_first['x'])

def main():
  current_route = router.get_url_route()
  with st.sidebar:
    if st.button('직장 선택'):
      router.route('/select')
    elif st.button('인프라 확인'):
      router.route('/map')

if __name__ == "__main__":
  API_KEY = "a2f453d9ca3702e131a49655686b4dc8"
  router = initRouter()
  router.show_route_view()
  
  main()
