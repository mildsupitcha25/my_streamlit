import streamlit as st
import pandas as pd
import numpy as np

st.title('Starbuck')



data_stb = ('https://github.com/mildsupitcha25/my_streamlit/raw/main/directory.csv')

@st.cache_data
def load_data(nrows):
    
    data = pd.read_csv(data_stb, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Map of all branches')
map_data = data[['latitude', 'longitude']].dropna()

st.map(map_data)

