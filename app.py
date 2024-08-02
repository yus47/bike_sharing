import numpy as np
import pandas as pd
import streamlit as st
import datetime as dt
import pickle

st.title('Prediksi Jumlah Sepeda yang Sedang Beredar')

if 'model' not in st.session_state:
    model = pickle.load(open('Bike_Sharing_Log_Model.sav', 'rb'))
    st.session_state['model'] = model

st.header('Masukkan kondisi cuaca')
dteday = st.date_input('Masukkan tanggal (YYYY-MM-DD)', value = None)
hum = st.number_input('Masukkan tingkat kelembapan (0 sampai 1)', min_value = 0.0, max_value = 1.0)
weathersit = st.radio('Masukkan kondisi cuaca; 1: sangat bagus, 2: berkabut, 3: hujan / salju', [1,2,3])
season = st.radio('Masukkan musim; 1: musim dingin, 2: musim semi, 3: musim panas, 4: musim gugur', [1,2,3,4])
atemp = st.number_input('Masukkan suhu yang dirasakan (mohon normalisasi dulu menjadi skala 0-1)',min_value = 0.0, max_value = 1.0)
hr = st.radio('Masukkan jam berapa data diambil (0-23)', list(range(0,24)))

dteday_datetime = dteday
year = dteday_datetime.dt.year
month = dteday_datetime.dt.month
day = dteday_datetime.dt.day
day = str(day)
day_week = dteday_datetime.dt.day_of_week.dtype=('object')
day_week = str(day_week)

hr_bin_ord = []
if(hr in [0,6,23]):
    hr_bin_ord = [1]
elif(hr in [1,2,3,4,5]):
    hr_bin_ord = [0]
elif(hr in [7,9,10,11]):
    hr_bin_ord = [3]
elif(hr in [8]):
    hr_bin_ord = [6]
elif(hr in [12,13,14,15]):
    hr_bin_ord = [4]
elif(hr in [16,19]):
    hr_bin_ord = [5]
elif(hr in [17,18]):
    hr_bin_ord = [7]
elif(hr in [20,21,22]):
    hr_bin_ord = [2]


if st.button('Prediksi Jumlah Sepeda yang Sedang Disewa'):
    data_dict = {
    'day': day,
    'day_week': day_week,
    'hr_bin_ord': hr_bin_ord,
    'season': season,
    'weathersit': weathersit,
    'hum': hum,
    'atemp': atemp
             }
    data = pd.DataFrame(data_dict, index=[0])
    result = st.session_state['model'].predict(data)
    st.write(f'Perkiraan Jumlah Sepeda yang Sedang Disewa adalah: {np.exp(result[0])} unit')
else:
    st.write('Masukkan kondisi waktu dan cuaca untuk memprediksi jumlah sepeda yang sedang disewa!')