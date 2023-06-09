#Import libraries
#from re import X
import streamlit as st
import scipy
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.figure_factory as ff



#Load and clean data
data = sns.load_dataset('penguins')
data['bill_length_mm'].fillna(data['bill_length_mm'].mean(), inplace=True)
data['bill_depth_mm'].fillna(data['bill_depth_mm'].mean(), inplace=True)
data['flipper_length_mm'].fillna(data['flipper_length_mm'].mean(), inplace=True)
data['body_mass_g'].fillna(data['body_mass_g'].mean(), inplace=True)
data['sex'].fillna(data['sex'].value_counts().index[0], inplace=True)


#Creating more user-friendly option labels
data.rename(columns = 
    {"flipper_length_mm": "Flipper Length",  
    "bill_length_mm":"Bill Length",
    "bill_depth_mm":"Bill Depth",
    "body_mass_g":"Body Mass",
    "island":"Island",
    "sex":"Sex",
    "species":"Species"},
    inplace = True)
featureset = ['Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass', 'Island', 'Sex', 'Species']
graphset = ["Histogram", "Box Plot", "Enhanced Box Plot", "Strip Plot", "Violin Plot", "Swarm Plot"]

st.set_page_config(page_title="703_Demo", page_icon="🧊", layout="wide", initial_sidebar_state="expanded", menu_items={'Get Help': 'https://github.com/GMU-instructor/Teaching_public','Report a bug': "https://github.com/GMU-instructor/Teaching_public",'About': "# For CSI 703. This is an *extremely* cool app!"})

#Give our dashboard a title
st.title('Visualization dashboard')

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
    #('Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass', 'Island', 'Sex', 'Species'))
    #x = featureset1
#    if genre != "Histogram":
#        y = st.selectbox("Feature for y:", featureset1, key="f2l")
#        hue = st.selectbox("Feature for hue:", (featureset1), key="h2l")
#    if genre == "Histogram": 
#        kde = st.selectbox("Do you want to add a kde?", (True, False), key="k1")
#        color = st.color_picker('Pick a color for Plot 1', key="c1")
    if genre != "Histogram":
        #y = st.radio("Feature for y:", ('Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass', 'Island', 'Sex', 'Species'))
        #hue = st.radio("Feature for hue:", ('Island', 'Sex', 'Species'))
        x = st.radio(
        "Feature for x:",
        ('Island', 'Sex', 'Species'))
    if genre == "Histogram": 
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'), key="k1")
        x = st.radio(
        "Feature for x:",
        ('Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass', 'Island', 'Sex', 'Species'))
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'))
        #color = st.color_picker('Pick a color for Plot 1', key="c1")
with col2:
    if genre != "Histogram":
        #y = st.radio("Feature for y:", ('Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass', 'Island', 'Sex', 'Species'))
        y = st.radio("Feature for y:", ('Flipper Length', 'Bill Length', 'Bill Depth', 'Body Mass'))
        hue = st.radio("Feature for hue:", ('Island', 'Sex', 'Species'))
    if genre == "Histogram": 
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'), key="k1")
        #kde = st.radio("Do you want to add a kde?", ('True', 'False'))
        #kde = kde
        color = st.color_picker('Pick a color for Plot 1', key="c1")
    fig = plt.figure(figsize=(7, 5))
    if genre == "Histogram": sns.histplot(data = data, x = x, kde = 'True', color = color)
    #if genre == "Histogram": sns.histplot(data = data, x = x, kde = kde, color = color)
    if genre == "Box Plot": sns.boxplot(data = data, x = x, y = y, hue = hue)
    if genre == "Enhanced Box Plot": sns.boxenplot(data = data, x = x, y = y, hue = hue)
    if genre == "Strip Plot": sns.stripplot(data = data, x = x, y = y, hue = hue)  
    if genre == "Violin Plot": sns.violinplot(data = data, x = x, y = y, hue = hue)
    if genre == "Swarm Plot": sns.swarmplot(data = data, x = x, y = y, hue = hue)
with st.container():    
    plt.title(title)
    st.pyplot(fig)



col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('Penguins on Torgersen Island')
    df1 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-64.77167, -64.075],columns=['lat', 'lon'])
    st.map(df1,zoom=10)
with col2:
    st.subheader('Penguins on Dream Island')
    df2 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-64.733333, -64.233333],columns=['lat', 'lon'])
    st.map(df2,zoom=10)
with col3:
    st.subheader('Penguins on Biscoe Islands')
    df3 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-65.410155, -65.359285],columns=['lat', 'lon'])
    st.map(df3,zoom=10)
    


#with st.container():
#    df1 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-64.77167, -64.075],columns=['lat', 'lon'])
#    df2 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-64.733333, -64.233333],columns=['lat', 'lon'])
#    df3 = pd.DataFrame(np.random.randn(30, 2) / [400, 400] + [-65.410155, -65.359285],columns=['lat', 'lon'])
#    df4 = pd.concat([df1, df2, df3], axis=0)
#   st.map(df4)