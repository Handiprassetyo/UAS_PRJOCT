import pandas as pd
import plotly.express as px
import streamlit as st
import base64
import numpy as np
import datetime
import plotly.graph_objects as go
st.set_page_config(page_title="Uas Kelompok 1",
                 layout= "wide",
                )
data = pd.read_csv('C:/Users/20200/Desktop/uas/DATA PRODUK EDIFIER TRAINING (2).csv', sep=';')

st.title( "Uas Kelompok")
st.title( "TABEL PRODUK EDIFIER")
def convert_df(df):
   return data.to_csv(index=False).encode('utf-8')


csv = convert_df(data)

st.dataframe(data)
st.sidebar.header("Filter:")
nama_produk = st.sidebar.multiselect(
    "Select the nama_produk:",
     options=data["nama_produk"].unique(),
     default=data["nama_produk"].unique()
    )
#------Ganti tanggal masuk-----#
tanggal_masuk = st.sidebar.multiselect(
    "Select the tanggal masuk:",
     options=data["tanggal_masuk"].unique(),
     default=data["tanggal_masuk"].unique()
    )
#--------ganti kuantitas terjual------#
kuantitas_terjual = st.sidebar.multiselect(
    "Select the kuantitas terjual:",
     options=data["kuantitas_terjual"].unique(),
     default=data["kuantitas_terjual"].unique()
    )

df_selection=data.query(
  "nama_produk== @nama_produk & tanggal_masuk== @tanggal_masuk & kuantitas_terjual == @kuantitas_terjual"
)
st.dataframe(df_selection)

st.title("grafik")

data1 = go.Figure()

data1.add_trace(go.Scatter(x=data.tanggal_masuk, y=data.kuantitas_terjual,
                            marker={"color":"tomato"},
                            mode="lines"))
data1.update_layout(height=500,
                     xaxis_title="tanggal_masuk",
                     yaxis_title="kuantitas_terjual",
                     title="DATA PRODUK EDIFIER TRAINING")
st.plotly_chart(data1)
