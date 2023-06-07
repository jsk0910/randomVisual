import streamlit as st
import numpy as np
import pandas as pd

def initialize():
  st.title('Random Visual')
  
numberOfRV = 0

if __name__ == "__main__":
  plusbutton = False
  initialize()
  with st.sidebar:
    plusbutton = st.button('추가')
    if plusbutton == True:
      numberOfRV += 1
      st.slider(f'x{numberOfRV}:', 0, 1000)
      plusbutton = False
  plusbutton
