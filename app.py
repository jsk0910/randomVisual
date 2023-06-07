import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame()

if __name__ == "__main__":
  st.title('Random Visual')
  st.caption('열의 이름을 작성합니다, 여러 개의 열인 경우 콤마(,)로 구분해주세요')
  t = st.text_input('데이터 이름')
  t1 = t.split(',')
  st.caption('열에 들어갈 데이터를 작성합니다, 여러 개의 열인 경우 콤마(,)로 구분해주세요')
  d = st.text_input('데이터')
  d1 = d.split(',')
  for i in range(len(t1)):
    l = list(map(int, d1[i].split()))
    df[str(t1[i])] = l
  st.dataframe(df)
  
  choose = st.radio('그래프 형태 고르기', ['line-chart', 'area-chart', 'bar-chart'])
  if choose == 'line-chart':
    st.line_chart(df)
  if choose == 'area-chart':
    st.area_chart(df)
  if choose == 'bar-chart':
    st.bar_chart(df)
