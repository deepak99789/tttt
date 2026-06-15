import streamlit as st
import plotly.graph_objects as go
from scanner import get_processed_data, detect_zones
from bot import send_alert
from tickers import TICKERS

st.set_page_config(layout="wide")
st.title("🎯 Ultimate Multi-Asset Scanner")

asset_cat = st.sidebar.selectbox("Market Category", list(TICKERS.keys()))
symbol = st.sidebar.selectbox("Select Symbol", TICKERS[asset_cat])
tf = st.sidebar.selectbox("Timeframe", ["5m", "75m", "125m", "4h", "1d"])

if st.sidebar.button("Start Scan"):
    df = get_processed_data(symbol, tf)
    zones = detect_zones(df, symbol)
    
    st.write(f"### Results for {symbol}")
    st.write(f"Zones detected: {len(zones)}")
    for z in zones:
        send_alert(z)
        st.success(f"Alert sent for {z['Type']} zone at {z['Proximal']:.2f}")
    
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    st.plotly_chart(fig, use_container_width=True)
