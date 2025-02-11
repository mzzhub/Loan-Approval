import streamlit as st
import pickle
import pandas as pd

st.title('Loan Eligiblity Test')

with open("kaggle_model.pkl", "rb") as f:
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
previous_defaults = st.radio("**Black mark**", ("Yes", "No"), help = "Previous loan repay faliure on record")

dict_input = {
    'person_age' : age,
    'person_gender' : gender,
    'person_education' : education,
    'person_income' : income,
    'person_emp_exp' : experience,
    'person_home_ownership' : ownership,
    'loan_amnt' : amount,
    'loan_intent' : type,
    'loan_int_rate' : rate,
    'cb_person_cred_hist_length' : cbl,
    'credit_score' : credit_score,
    'previous_loan_defaults_on_file' : previous_defaults
    }

df_input = pd.DataFrame([dict_input])

st.write("From dictonary")
st.dataframe(df_input)

object_columns = df_input.select_dtypes(include = ["object"]).columns
df_dummies = pd.get_dummies(df_input, columns = object_columns)

feature_columns = ['person_age', 'person_income', 'person_emp_exp', 'loan_amnt',
       'loan_int_rate', 'cb_person_cred_hist_length', 'credit_score',
       'person_gender_Male', 'person_education_Bachelor',
       'person_education_Doctorate', 'person_education_High School',
       'person_education_Master', 'person_home_ownership_Other',
       'person_home_ownership_Own', 'person_home_ownership_Rent',
       'loan_intent_Education', 'loan_intent_Home improvement',
       'loan_intent_Medical', 'loan_intent_Personal', 'loan_intent_Venture',
       'previous_loan_defaults_on_file_Yes']

df_dummies = df_dummies.reindex(columns = feature_columns, fill_value = 0)
st.write("after reindex")
st.dataframe(df_dummies)

# for col in feature_columns:
#     if col not in df_dummies.columns:
#         df_dummies[col] = 0

# st.write("after for loop 01")
# st.dataframe(df_dummies)

drop_first_columns = ["person_gender_Female", "person_education_Associate", "person_home_ownership_Mortage", "loan_intent_Debt consolidation", "previous_loan_defaults_on_file_No"]
for i in drop_first_columns:
    if i in df_dummies.columns:
        df_dummies = df_dummies.drop(i, axis = 1)

st.write("after for loop 02")
st.dataframe(df_dummies)

st.write("after dummies")
st.dataframe(df_dummies)

st.write(df_dummies.columns)
output = lrc.predict(df_dummies)
st.write(output)

if output == 1:
    st.write("Approved")
else:
    st.write("Not approved")