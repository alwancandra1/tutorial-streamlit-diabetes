# python -m streamlit run streamlit_diabetes.py

import pickle
import streamlit as st

# Membaca Model
diabetes_model = pickle.load(open('diabetes_model_svm.sav', 'rb'))

# Judul
st.title('Data Mining Prediksi Diabetes')

# Membuat Kolom
col1, col2 = st.columns(2)
with col1:
    Pregnancies = st.number_input('Nilai Pregnancies :')
with col1:
    Glucose = st.number_input('Nilai Glucose :')
with col1:
    BloodPressure = st.number_input('Nilai BloodPressure :')
with col1:
    SkinThickness = st.number_input('Nilai SkinThickness :')
with col2:
    Insulin = st.number_input('Nilai Insulin :')
with col2:
    BMI = st.number_input('Nilai BMI :')
with col2:
    DiabetesPedigreeFunction = st.number_input('Nilai DiabetesPedigreeFunction :')
with col2:
    Age = st.number_input('Nilai Age :')

# Code untuk prediks
diab_diag = ' '

# Tombol
if st.button('Mulai Prediksi'):
    diab_predict = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]])

    if diab_predict == 0:
        st.title("Pasien tidak terkena Diabetes")
    elif diab_predict == 1:
        st.title("Pasien terkena Diabetes")