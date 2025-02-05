import streamlit as st
import pickle

st.title('Loan Eligiblity Test')

with open("model.pkl", "rb") as f:
    lrc = pickle.load(f)

age = st.slider("**Age**", 20, 144, 30)
gender = st.radio("**Gender**", ("Male", "Female"))
education = st.selectbox("**Education**", ('High school', 'Associate', 'Bachelor', 'Master', 'Doctorate'), placeholder = "Select your educational qualification", index = None)
income = st.number_input("**Annual Income** in dollars", 8000, 7200000, placeholder = "Type your annual income")
experience = st.number_input("**Employment experience**", 0, 125, help = "in years")
ownership = st.selectbox("**House ownership**", ('Own', 'Mortage', 'Rent', 'Other'), placeholder ="Select your house ownership type", index = None)
amount = st.number_input("**Requried loan amount** in dollars", 500, 35000)
type = st.selectbox("**Loan type**", ('Education', 'Medical', 'Home improvement', 'Debt consolidation', 'Personal', 'Venture'), placeholder = "Select your purpose of loan", index = None)
rate = st.number_input("**Intrest rate**", 5.00, 20.00)
cbl = st.number_input("**Credit History Length**", 2, 30, help = "Credit Bureau's credit history length")
credit_score = st.number_input("**Credit score**", 390, 850)
defaults = st.radio("**Black mark**", ("Yes", "No"), help = "Previous loan repay faliure on record")

