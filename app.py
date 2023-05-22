import streamlit as st

st.title('Random Visual')
with st.sidebar:
  x = st.slider('Pick a number', 0, 1000)
