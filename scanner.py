import yfinance as yf

def get_processed_data(symbol, timeframe):
    df = yf.download(symbol, period="1mo", interval="5m")
    tf_map = {"5m": "5min", "75m": "75min", "125m": "125min", "4h": "4H", "1d": "1D"}
    rule = tf_map.get(timeframe, "15min")
    return df.resample(rule).agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'}).dropna()

def detect_zones(df, symbol):
    zones = []
    for i in range(1, len(df) - 2):
        leg_in, base, leg_out = df.iloc[i-1], df.iloc[i], df.iloc[i+1]
        # Logic: Agar Leg-out ka body size Leg-in se bada hai
        if abs(leg_out['Close'] - leg_out['Open']) > abs(leg_in['Close'] - leg_in['Open']):
            zones.append({'Symbol': symbol, 'Proximal': base['High'], 'Distal': base['Low'], 
                          'Type': 'Demand' if leg_out['Close'] > leg_out['Open'] else 'Supply'})
    return zones
