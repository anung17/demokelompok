import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("Pertemuan 10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = {
    "GOOGL": 'Google',
    'AAPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDonald's Corp",
    'META': "Meta Platforms Inc",
    'TLKM.JK': "Telkom Indonesia (Persero) Tbk PT",
    'BBNI.JK': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted( kamus_ticker.keys() )
)

st.write(ticker_symbol)
#ticker_symbol = 'GOOGL'
#ticker_symbol = 'AAPL'

ticker_data = yf.Ticker( ticker_symbol )
# standar ISO untuk tanggal
tgl_mulai = str(
    st.date_input(
        'Tanggal mulai:',
        value = date.today()
    )
)
tgl_akhir = str(
    st.date_input(
        'Tanggal akhir:',
        value = date.today()
    )
)

df_ticker = ticker_data.history(
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('Tampilkan tabel')
#st.write(pilihan_tampil_tabel)

if pilihan_tampil_tabel == True:
    st.write("## Lima Data Awal")
    st.write( df_ticker.head() )

st.write(f"## Visualisasi Pergerakan Saham {kamus_ticker[ticker_symbol]}")

tampil_grafik = st.checkbox('Tampilkan Line Plot')
if tampil_grafik == True:
    atribut = st.multiselect(
        'Silahkan pilih atribut yang akan divisualisasikan',
        ['Open', 'Close', 'Low', 'High']
    )
    grafik = px.line(
        df,
        y = atribut,
        title = f'Harga saham {kamus_ticker[ticker_symbol]}'
    )
    st.plotly_chart( grafik )

