import yfinance as yf
import streamlit as st
import pandas as pandas

st.write("""
# Simple Stock Price APP

Show are the stock **closing** price and **volume** of Bitcoin between January 2020 and December 2022!

""")

st.caption('Code by DataProfessor Channel')


tickerSymbol ="BTC-USD"

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period="Id", start='2020-1-01', end="2022-12-31")

st.header(":grey[-----------------------------------------------------------------]")
st.header('**Close Graph**')
st.line_chart(tickerDF.Close)
st.header(":grey[-----------------------------------------------------------------]")
st.header('**Volume Graph**')
st.line_chart(tickerDF.Volume)
st.header(":grey[-----------------------------------------------------------------]")


