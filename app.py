import streamlit as st
import numpy as np
import pandas as pd

data = []

df = pd.DataFrame()

if __name__ == "__main__":
  t = st.text_input('데이터 이름')
  d = st.text_input('데이터')
  l = list(map(int, d.split()))
  data.append({t: [l]})
  df = pd.DataFrame(data)
  st.dataframe(df)
