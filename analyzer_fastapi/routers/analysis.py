from fastapi import APIRouter, Query
import yfinance as yf
import pandas as pd
import ta

router = APIRouter()

@router.get("/")
def analyze_asset(symbol: str = Query(..., description="Ticker de l'actif à analyser")):
    df = yf.download(symbol, period="3mo", interval="1d")

    if df.empty:
        return {"error": "Données indisponibles pour ce symbole."}

    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['EMA50'] = ta.trend.EMAIndicator(close=df['Close'], window=50).ema_indicator()
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close']).rsi()
    macd = ta.trend.MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_signal'] = macd.macd_signal()

    return {
        "last_close": df['Close'].iloc[-1],
        "ema20": df['EMA20'].iloc[-1],
        "ema50": df['EMA50'].iloc[-1],
        "rsi": df['RSI'].iloc[-1],
        "macd": df['MACD'].iloc[-1],
        "macd_signal": df['MACD_signal'].iloc[-1]
    }