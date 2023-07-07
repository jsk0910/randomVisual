import folium
import streamlit as st

from streamlit_folium import st_folium
import extra_streamlit_components as stx

import json
import requests
import datetime

def initRouter():
  return stx.Router({'/select': selectWork, '/map': map})

@st.cache(allow_output_mutation=True)
def get_manager():
    return stx.CookieManager()

# define 직장선택
def selectWork():
  st.title('selectWork')
  cookie_manager = get_manager()
  if st.button('선택'):
    cookie_manager.set("work", "부산광역시 해운대구 수영강변대로 140", expires_at=datetime.datetime(year=2022, month=2, day=2))

# define 지도 탭
def map():
  cookie_manager = get_manager()
  cookies = cookie_manager.get_all()
  address = cookie_manager.get("work")
  st.title('Map')
  center_xy = list(addr_to_lat_lon(address))
  m = folium.Map(location=center_xy, zoom_start=16)
  folium.Marker(center_xy, 
                popup="회사명",
                tooltip="회사명"
                ).add_to(m)

  st_folium(m, width=725, returned_objects=[])

def addr_to_lat_lon(addr):
  url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
  headers = {"Authorization": "KakaoAK " + API_KEY}
  result = json.loads(str(requests.get(url, headers=headers).text))
  match_first = result['documents'][0]['address']
  return float(match_first['y']), float(match_first['x'])

def main():
  router = initRouter()
  router.show_route_view()
  current_route = router.get_url_route()
  with st.sidebar:
    if st.button('직장 선택'):
      router.route('/select')
    elif st.button('탭'):
      router.route('/map')

if __name__ == "__main__":
  API_KEY = "a2f453d9ca3702e131a49655686b4dc8"
  main()
