import streamlit as st
import pickle

st.title('Loan Eligiblity Test')

with open("model.pkl", "rb") as f:
    lrc = pickle.load(f)

age = st.slider("Age", 20, 144, 30)
gender = st.radio("Gender", ("Male", "Female"))
education = st.selectbox("Education", ('High school', 'Associate', 'Bachelor', 'Master', 'Doctorate'), placeholder = "Select your educational qualification")
income = st.number_input("Annual Income", 8000, 7200000, help = "in dollars")
experience = st.number_input("Employment experience", 0, 125, help = "in years")
ownership = st.selectbox("House ownership type", ('Own', 'Mortage', 'Rent', 'Other'))
amount = st.number_input("Requried loan amount", 500, 35000, help = "in dollars")
type = st.selectbox("Loan type", ('Education', 'Medical', 'Home improvement', 'Debt consolidation', 'Personal', 'Venture'))
# rate = 
# cbl = "Credit Bureau: Person's Credit History Length"
# credit_score = 
# defaults = "Previous Loan Defaults on File"
