import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!
""")

# Defining a tikcer symbol
tickerSymbol = 'GOOGL'

# Getting data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Getting the historical prices for this ticker
tickerDf = tickerData.history(period = '1mo',start = '2024-2-1',end = '2025-2-28')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf['Close'])

st.write("""
## Volume Pricing
""")
st.line_chart(tickerDf['Volume'])