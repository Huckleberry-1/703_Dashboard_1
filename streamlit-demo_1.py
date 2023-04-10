#Import libraries
#from re import X
import streamlit as st
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px



#Load and clean data
data = sns.load_dataset('penguins')
data['bill_length_mm'].fillna(data['bill_length_mm'].mean(), inplace=True)
data['bill_depth_mm'].fillna(data['bill_depth_mm'].mean(), inplace=True)
data['flipper_length_mm'].fillna(data['flipper_length_mm'].mean(), inplace=True)
data['body_mass_g'].fillna(data['body_mass_g'].mean(), inplace=True)
data['sex'].fillna(data['sex'].value_counts().index[0], inplace=True)


#Creating more user-friendly option labels
data.rename(columns = 
    {"flipper_length_mm": "flipper length",  
    "bill_length_mm":"bill length",
    "bill_depth_mm":"bill depth",
    "body_mass_g":"body mass"},
    inplace = True)
featureset = ['flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species']
graphset = ["Histogram", "Box Plot", "Enhanced Box Plot", "Strip Plot", "Violin Plot", "Swarm Plot"]

st.set_page_config(page_title="703_Demo", page_icon="🧊", layout="wide", initial_sidebar_state="expanded", menu_items={'Get Help': 'https://github.com/GMU-instructor/Teaching_public','Report a bug': "https://github.com/GMU-instructor/Teaching_public",'About': "# This is a header. This is an *extremely* cool app!"})

#Give our dashboard a title
st.title('Customer dashboard')

#Show the raw data
st.subheader('Raw data')
st.write(data)

#Let the user choose graph, features, etc.
st.subheader('Visualization')
with st.container():
    title = st.text_input('Enter a title for the chart')
    st.subheader('Choices')
col1, col2 = st.columns(2)

with col1:
    #st.subheader('Choices')
    #title = st.text_input('Enter a title for the chart')
    genre = st.radio(
    "What type of plot do you want",
    ("Histogram", "Box Plot", "Enhanced Box Plot", "Strip Plot", "Violin Plot", "Swarm Plot"))
    
    #x = st.radio(
    #"Feature for x:",
    #('flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species'))
    #x = featureset1
#    if genre != "Histogram":
#        y = st.selectbox("Feature for y:", featureset1, key="f2l")
#        hue = st.selectbox("Feature for hue:", (featureset1), key="h2l")
#    if genre == "Histogram": 
#        kde = st.selectbox("Do you want to add a kde?", (True, False), key="k1")
#        color = st.color_picker('Pick a color for Plot 1', key="c1")
    if genre != "Histogram":
        #y = st.radio("Feature for y:", ('flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species'))
        #hue = st.radio("Feature for hue:", ('island', 'sex', 'species'))
        x = st.radio(
        "Feature for x:",
        ('island', 'sex', 'species'))
    if genre == "Histogram": 
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'), key="k1")
        x = st.radio(
        "Feature for x:",
        ('flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species'))
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'))
        #color = st.color_picker('Pick a color for Plot 1', key="c1")
with col2:
    if genre != "Histogram":
        #y = st.radio("Feature for y:", ('flipper length', 'bill length', 'bill depth', 'body mass', 'island', 'sex', 'species'))
        y = st.radio("Feature for y:", ('flipper length', 'bill length', 'bill depth', 'body mass'))
        hue = st.radio("Feature for hue:", ('island', 'sex', 'species'))
    if genre == "Histogram": 
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'), key="k1")
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'))
        kde = kde
        color = st.color_picker('Pick a color for Plot 1', key="c1")
    fig = plt.figure(figsize=(7, 5))
    if genre == "Histogram": sns.histplot(data = data, x = x, kde = kde, color = color)
    if genre == "Box Plot": sns.boxplot(data = data, x = x, y = y, hue = hue)
    if genre == "Enhanced Box Plot": sns.boxenplot(data = data, x = x, y = y, hue = hue)
    if genre == "Strip Plot": sns.stripplot(data = data, x = x, y = y, hue = hue)  
    if genre == "Violin Plot": sns.violinplot(data = data, x = x, y = y, hue = hue)
    if genre == "Swarm Plot": sns.swarmplot(data = data, x = x, y = y, hue = hue)
with st.container():    
    plt.title(title)
    st.pyplot(fig)