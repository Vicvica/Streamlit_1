import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns


st.set_page_config(
    page_title="Quête Streamlit",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Quête Streamlit")
st.write("Les voitures vroum vroum")
# Charger les données
df = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

st.sidebar.header("Please Filter Here:")
country = st.sidebar.multiselect(
    "Select Country:",
    options=df["continent"].unique(),
    default=df["continent"].unique()
)
# Filter the DataFrame based on selected countries
filtered_df = df[df['continent'].isin(country)]

st.write(filtered_df)


#Histogramme
fig_histogram = px.histogram(filtered_df, x='mpg', nbins=30,
                             title='Distribution de Miles per Gallon',
                             labels={'mpg': 'Miles per Gallon'})
st.plotly_chart(fig_histogram, use_container_width=True)

# Graphique Box
fig_box = px.box(filtered_df, x='continent', y='mpg', color='continent',
                 title='Miles per Gallon by Continent',
                 labels={'mpg': 'Miles per Gallon'})
st.plotly_chart(fig_box, use_container_width=True)


# Graphique Bar
fig_bar = px.bar(filtered_df, x='continent', y='hp', color='continent',
                   title='Horsepower by Continent',
                   labels={'horsepower': 'Horsepower'})
st.plotly_chart(fig_bar, use_container_width=True)