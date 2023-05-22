import streamlit as st
import numpy as np
import pandas as pd
import streamlit_folium as sf
import requests
import json

x = 0
location = ""

def detectLocation(keyword): # 위치와 타입을 인식
  if !keyword: 
    return ("PLACE", "서울특별시청")

def locationSearch(key, keyword):
  endPoint = "http://api.vworld.kr/req/search?" # vworld endPoint
  basicInfo = "service=search&request=search&version=2.0&format=json&errorformat=json" # 기본적인 리퀘스트 정보
  type, loc = detectLocation(location) # 리퀘스트 타입
  
  url = f'{endPoint}{basicInfo}&type={type}&query={loc}&key={key}'
  
  result = requests.get(url).json()
  st.write(result)

st.title('Random Visual')

with st.sidebar:
  x = st.slider('Pick a number', 0, 1000)
  location = st.text_input('검색하려는 위치')
  
locationSearch("4F685D82-6BF7-3DA1-A19C-8F630815C7B0",location)
