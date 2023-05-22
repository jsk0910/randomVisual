import streamlit as st
import numpy as np
import pandas as pd
import streamlit_folium as sf

def chooseLocationType(keyword):
  

def locationSearch(key, keyword):
  endPoint = "http://api.vworld.kr/req/search?" # vworld endPoint
  basicInfo = "service=search&request=search&version=2.0&format=json&errorformat=json" # 기본적인 리퀘스트 정보
  type = "ADDRESS" # 리퀘스트 타입

st.title('Random Visual')
x = 0
location = ""

with st.sidebar:
  x = st.slider('Pick a number', 0, 1000)
  location = st.text_input('검색하려는 위치')

