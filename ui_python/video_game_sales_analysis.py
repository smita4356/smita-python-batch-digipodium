import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

st.title('video game sales analysis')
@st.cache

def load_data():
    data = pd.read_csv('vgsales.csv.zip')
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading completed...!')
st.subheader('Raw data')
st.write(data)
    
st.subheader ('genre sold the most globally')    
data[["Genre","Global_Sales"]].groupby("Genre").sum()


plt.pie(data.Genre.value_counts(), labels=data.Genre.value_counts().index, autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2)
plt.title('Video Game Genre Share')
plt.ylabel(' ')
plt.show()




