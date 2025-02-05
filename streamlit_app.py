import streamlit as st
import pickle

st.title('Loan Eligiblity Test')

with open("model.pkl", "rb") as f:
    lrc = pickle.load(f)

age = st.slider("Age", 20, 144, 30)
gender = st.radio("Gender", ("Male", "Female"))
education = st.selectbox("Education", ('High School', 'Associate', 'Bachelor', 'Master', 'Doctorate'), placeholder = "Select your educational qualification")
# income = 
# experiance = 
# ownership = 
# amount = 
# purpose = 
# rate = 
# cbl = "Credit Bureau: Person's Credit History Length"
# credit_score = 
# defaults = "Previous Loan Defaults on File"
