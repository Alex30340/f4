from fastapi import APIRouter, Query
from utils.indicators import get_technical_indicators
import yfinance as yf

router = APIRouter()

@router.get("/")
def analyse_asset(
    symbol: str = Query(..., description="Symbole de l'actif (ex: BTC-USD)"),
    period: str = Query("3mo", description="Période (ex: 1mo, 3mo, 6mo)"),
    interval: str = Query("1d", description="Intervalle (ex: 1d, 1h, 15m)")
):
    df = yf.download(symbol, period=period, interval=interval)
    if df.empty:
        return {"error": "Aucune donnée disponible."}
    
    result = get_technical_indicators(df)
    return result
