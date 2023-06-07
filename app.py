import streamlit as st
import numpy as np
import pandas as pd

def initialize():
  st.title('Random Visual')

if __name__ == "__main__":
  initialize()
  with st.sidebar:
    if st.button('추가'):
      t = st.text_input('데이터 이름')
      value = st.text_area('데이터')
