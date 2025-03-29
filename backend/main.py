from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
import yfinance as yf
import ta

app = FastAPI()


class GraphData(BaseModel):
    symbol: str

# ✅ Page d'accueil ("/") qui redirige vers la doc Swagger
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>F4 Analyzer</title>
        </head>
        <body style="font-family:sans-serif; text-align:center; padding:50px;">
            <h1>Bienvenue sur F4 Analyzer 📊</h1>
            <p>Utilisez <a href="/docs">/docs</a> pour explorer l’API ou accédez directement à <code>/graph/TSLA</code></p>
        </body>
    </html>
    """

@app.get("/graph/{symbol}")
async def get_graph(symbol: str):
    df = yf.download(symbol, period="3mo", interval="1d")
    
    df['EMA20'] = ta.trend.EMAIndicator(close=df['Close'], window=20).ema_indicator()
    df['EMA50'] = ta.trend.EMAIndicator(close=df['Close'], window=50).ema_indicator()
    
    data = [
        {"x": df.index.strftime('%Y-%m-%d').tolist(), "y": df['Close'].tolist(), "type": "scatter", "mode": "lines", "name": "Close Price"},
        {"x": df.index.strftime('%Y-%m-%d').tolist(), "y": df['EMA20'].tolist(), "type": "scatter", "mode": "lines", "name": "EMA20"}
    ]
    
    layout = {
        "title": f"{symbol} - Graphique",
        "xaxis": {"title": "Date"},
        "yaxis": {"title": "Prix"}
    }
    
    return {"data": data, "layout": layout}
