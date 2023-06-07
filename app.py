import streamlit as st
import numpy as np
import pandas as pd

def initialize():
  st.title('Random Visual')

if __name__ == "__main__":
  plusbutton = False
  initialize()
  with st.sidebar:
    plusbutton = st.button('추가')
  plusbutton
