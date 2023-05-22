import streamlit as st
import numpy as np
import pandas as pd
import streamlit-folium as sf

st.title('Random Visual')
x = 0
with st.sidebar:
  x = st.slider('Pick a number', 0, 1000)
