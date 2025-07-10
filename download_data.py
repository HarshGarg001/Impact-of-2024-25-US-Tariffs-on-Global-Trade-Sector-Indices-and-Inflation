Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import yfinance as yf
... import pandas as pd
... 
... # ------------------------------
... # Define the assets and names
... # ------------------------------
... assets = {
...     "TSLA": "Tesla",
...     "BYDDY": "BYD",
...     "NIO": "NIO",
...     "NVDA": "Nvidia",
...     "TSM": "TSMC",
...     "ALB": "Albemarle",
...     "LIT": "LIT_ETF",
...     "JSWSTEEL.NS": "JSW_Steel",
...     "TATAMOTORS.NS": "Tata_Motors",
...     "REMX": "RareEarths_REMX",
...     "HG=F": "Copper_HG"
... }
... 
... # ------------------------------
... # Define date range
... # ------------------------------
... start_date = "2024-03-01"
... end_date = "2024-07-01"
... 
... # ------------------------------
... # Download data and save to CSV
... # ------------------------------
... for symbol, name in assets.items():
...     try:
...         print(f"Downloading {name}...")
...         df = yf.download(symbol, start=start_date, end=end_date, interval="1d", progress=False)
... 
...         if df.empty:
...             print(f"❌ No data for {symbol} — skipping.")
            continue

        # Optional: Use monthly data
        # df = df.resample('M').last()

        # Keep only Adjusted Close price
        df = df[['Adj Close']].rename(columns={"Adj Close": name})
        df.reset_index(inplace=True)

        # Save to CSV
        df.to_csv(f"{name}.csv", index=False)
        print(f"✅ Saved {name}.csv")

    except Exception as e:
        print(f"Error downloading {symbol}: {e}")

print("\nDownload complete.")
