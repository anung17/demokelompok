import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date, datetime, timedelta

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
    sorted( kamus_ticker.keys() ),
    index=3
)

st.write(ticker_symbol)

#tanggal_hari_ini = datetime.now()
tanggal_hari_ini = date.today()
satu_bulan_lalu = timedelta(days=28)
tanggal_sebulan_lalu = tanggal_hari_ini - satu_bulan_lalu

ticker_data = yf.Ticker( ticker_symbol )
# standar ISO untuk tanggal
tgl_mulai = str(
    st.date_input(
        'Tanggal mulai:',
        #value = date.today()
        value = tanggal_sebulan_lalu
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
    if not df_ticker.empty:
        st.write( df_ticker.head() )
    else:
        st.write('`DataFrame` is empty.')

st.write(f"## Visualisasi Pergerakan Saham {kamus_ticker[ticker_symbol]}")

tampil_grafik = st.checkbox('Tampilkan Line Plot', value=True)
if tampil_grafik == True and not df_ticker.empty:
    atribut = st.multiselect(
        'Silahkan pilih atribut yang akan divisualisasikan',
        ['Open', 'Close', 'Low', 'High'],
        default = ['Open', 'Close']
    )
    grafik = px.line(
        df_ticker,
        y = atribut,
        title = f'Harga saham {kamus_ticker[ticker_symbol]}'
    )
    st.plotly_chart( grafik )

