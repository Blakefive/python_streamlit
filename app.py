import streamlit as st
import pandas_datareader as pdr
from cryptocmd import CmcScraper
import plotly.express as px
from datetime import datetime

st.write('''
# 주식 데이터
마감 가격과 거래량을 차트로 보여줍니다.
''')

# https://finance.yahoo.com/quote/005930.KS?p=005930.KS
st.sidebar.header('Menu')

name = st.sidebar.selectbox('Name', ['samsung', 'apple','amazon'])
namedir = {'samsung':'005930.KS','apple':'AAPL','amazon':'AMZN'}

start_date = st.sidebar.date_input('Start date', datetime(2021, 1, 1))
end_date = st.sidebar.date_input('End date', datetime(2021, 1, 7))

df = pdr.get_data_yahoo(namedir[name], start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

st.write('# '+name)
st.line_chart(df.Close)
st.line_chart(df.Volume)

