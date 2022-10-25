import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data (1990) by Henian')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Median House Price:', 0, 500001, 200000)  # min, max, default

# create a multi select
ocean_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
income = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'),
    index=0)


# filter by population
df = df[df.median_house_value <= price_filter]

# filter by country
df = df[df.ocean_proximity.isin(ocean_filter)]

if income == 'Low':
    df = df[df.median_income <= 2.5]
elif income == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
elif income == 'High':
    df = df[df.median_income > 4.5] 

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value:')
fig, ax = plt.subplots()
pop_sum = df.median_house_value
pop_sum.plot.hist(bins=30)
st.pyplot(fig)