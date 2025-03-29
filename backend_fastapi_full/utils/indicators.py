import pandas as pd
import ta

def get_technical_indicators(df: pd.DataFrame) -> dict:
    df = df.copy()
    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['EMA50'] = ta.trend.EMAIndicator(close=df['Close'], window=50).ema_indicator()
    macd = ta.trend.MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close']).rsi()

    last_price = df['Close'].iloc[-1]
    tp = round(last_price * 1.05, 2)
    sl = round(last_price * 0.95, 2)
    rr_ratio = round((tp - last_price) / (last_price - sl), 2)

    return {
        "dernier_prix": last_price,
        "take_profit": tp,
        "stop_loss": sl,
        "risk_reward": rr_ratio,
        "indicateurs": {
            "RSI": round(df['RSI'].iloc[-1], 2),
            "MACD": round(df['MACD'].iloc[-1], 2),
            "EMA20": round(df['EMA20'].iloc[-1], 2),
            "EMA50": round(df['EMA50'].iloc[-1], 2)
        }
    }
