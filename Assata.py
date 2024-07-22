import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import plotly 
st.title("bonjour je me m'appele Assata")
st.write("## biographie")
st.write("La paresse ne doit pas être confondue avec l'otium (le loisir), ou plus précisément l'activité désintéressée, libérale, que les Romains opposaient au negotium (l'activité vénale, le commerce). L'otium est une vertu du lettré défendue par Cicéron et Sénèque et, surtout, un privilège indispensable pour exercer les activités du citoyen, participer à la vie de la cité et au brassage des idées, et que seule la possession de terres peut assurer.La paresse, en revanche, consiste à ne pas avoir envie de faire ce qu'il serait en principe nécessaire que l'on fasse, pour soi ou pour les autres, afin en général de mieux vivre. Le terme prend alors une connotation négative jusqu'à désigner un péché.Dans la tradition catholique, la paresse est souvent assimilée à l'un des sept péchés capitaux. En réalité, le catéchisme de l'Église catholique mentionne ce péché capital comme « paresse ou acédie ». Le mot « acédie », très peu utilisé de nos jours, et qui a même disparu de la plupart des dictionnaires, est traditionnellement utilisé par certains théologiens1 monastique (d'Évagre le Pontique à saint Thomas d'Aquin et jusqu'à la fin du Moyen Âge). Le terme acédie correspond à de la paresse spirituelle, ce qui est bien différent du sens moderne donné à ce péché par l'emploi du simple mot paresse au sein des 7 péchés capitaux2. ")
import plotly.express as px
df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()
st.plotly_chart(fig)
