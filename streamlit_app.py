import streamlit as st
import pickle

st.title('Loan Eligiblity Test')

with open("model.pkl", "rb") as f:
    lrc = pickle.load(f)
    
st.write("AGE")
age = st.slider("Age", 20, 144, 30)

