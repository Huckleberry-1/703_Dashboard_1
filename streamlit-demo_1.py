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

with st.container():
    # Add histogram data
    AB = [3400,3600,3800,3950,3800,3800,3550,3200,3150,3950,3500,4300,3450,4050,2900,3700,3550,3800,2850,3750,3150,4400,3600,4050,2850,3950,3350,4100,3725,4725,3075,4250,2925,3550,3750,3900,3175,4775,3825,4600,3200,4275,3900,4075]
    AD = [3250,3900,3300,3900,3325,4150,3950,3550,3300,4650,3150,3900,3100,4400,3000,4600,3425,2975,3450,4150,3350,3550,3800,3500,3950,3600,3550,4300,3400,4450,3300,4300,3700,4350,2900,4100,3500,4475,3425,3900,3175,3975,3400,4250,3400,3475,3050,3725,3000,3650,4250,3475,3450,3750,3700,4000]
    AT = [3750,3800,3250,4202,3450,3650,3625,4675,3475,4250,3300,3700,3200,3800,4400,3700,3450,4500,3325,4200,3050,4450,3600,3900,3550,4150,3700,4250,3700,3900,3550,4000,3200,4700,3800,4200,2900,3775,3350,3325,3150,3500,3450,3875,3050,4000,3275,4300,3050,4000,3325,3500]
    #x1 = np.random.randn(200) - 2
    #x2 = np.random.randn(200)
    #x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [AB, AD, AT]

    group_labels = ['AB', 'AD', 'AT']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 10, 10])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    df = pd.DataFrame(
        np.random.randn(50, 2) / [100, 100] + [-64.766667, -64.083333],
        columns=['lat', 'lon'])

    st.map(df)