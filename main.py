
from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf
import ta

app = FastAPI()

class GraphData(BaseModel):
    symbol: str

@app.get("/graph/{symbol}")
async def get_graph(symbol: str):
    df = yf.download(symbol, period="3mo", interval="1d")
    
    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['EMA50'] = ta.trend.EMAIndicator(close=df['Close'], window=50).ema_indicator()
    
    data = [
        {"x": df.index, "y": df['Close'], "type": "scatter", "mode": "lines", "name": "Close Price"},
        {"x": df.index, "y": df['EMA20'], "type": "scatter", "mode": "lines", "name": "EMA20"}
    ]
    
    layout = {
        "title": f"{symbol} - Graphique",
        "xaxis": {"title": "Date"},
        "yaxis": {"title": "Prix"}
    }
    
    return {"data": data, "layout": layout}
