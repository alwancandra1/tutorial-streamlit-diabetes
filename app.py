import streamlit as st
import pickle
import numpy as np

# import model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

# Brand Laptop
company = st.selectbox('Brand',df['Company'].unique())

# Tipe Laptop
type = st.selectbox('Type',df['TypeName'].unique())

# Ram
ram = st.selectbox('RAM (in GB)',[2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight (in KG)')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['Yes','No'])

# IPS
ips = st.selectbox('IPS',['Yes','No'])

# Screensize
#screen_size = st.number_input('Screen_size')

# resolution
resolution = st.selectbox('Screen Resolution',['1366x768', '1600x900', '1920x1080', '2304x1440', '2560x1440', '2560x1600'])

# cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

# hdd
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

# ssd
ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])

# gpu
gpu = st.selectbox('GPU',df['Gpu Brand'].unique())

# os
os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

# split nilai ppi dan query diubah ke integer
X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
#ppi = ((X_res**2)+(Y_res**2))**0.5/screen_size
ppi = ((X_res**2)+(Y_res**2))**0.5
#query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

# Prediksi Harga Laptop
query = query.reshape(1,12)
st.title("Predicted Price in Dollar : $ " + str(int(np.exp(pipe.predict(query)[0]))))
