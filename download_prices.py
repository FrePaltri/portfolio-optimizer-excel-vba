from pathlib import Path
import yfinance as yf

TICKERS = ["AAPL", "MSFT", "NVDA", "JPM", "KO", "XOM", "JNJ", "BRK-B", "GLD", "TLT"]
OUT = Path(__file__).parent / "prices.csv"

prices = yf.download(TICKERS, period="5y", auto_adjust=True, progress=False)["Close"]
prices = prices[TICKERS].dropna()   # stesso ordine dei ticker, solo giorni con tutti i prezzi
prices.to_csv(OUT, date_format="%Y-%m-%d")

print(f"Salvato: {OUT}")
print(f"{prices.shape[0]} righe, {prices.shape[1]} titoli")
print(prices.index[0].date(), "->", prices.index[-1].date())