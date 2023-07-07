import folium
import streamlit as st

from streamlit_folium import st_folium

import json
import requests

def addr_to_lat_lon(addr):
  url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
  headers = {"Authorization": "KakaoAK " + API_KEY}
  result = json.loads(str(requests.get(url, headers=headers).text))
  match_first = result['documents'][0]['address']
  return float(match_first['y']), float(match_first['x'])

API_KEY = "a2f453d9ca3702e131a49655686b4dc8"
center_xy = list(addr_to_lat_lon(address))
m = folium.Map(location=center_xy, zoom_start=16)
folium.Marker(center_xy, 
              popup="회사명",
              tooltip="회사명"
              ).add_to(m)

st_folium(m, width=725, returned_objects=[])
