import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame()

if __name__ == "__main__":
  t = st.text_input('데이터 이름')
  d = st.text_input('데이터')
  l = list(map(int, d.split()))
  df[str(t)] = l
  st.dataframe(df)
  
  choose = st.radio('그래프 형태 고르기', ['line-chart', 'area-chart'])
  if choose == 'line-chart':
    st.line_chart(df)
