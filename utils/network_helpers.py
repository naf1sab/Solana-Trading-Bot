# Network Helpers
async def get_sol_price_usd(session=None) -> float:
    """Fetch real SOL price with fallback APIs"""
    
    try:
        async with aiohttp.ClientSession() as s:
            url = "https://api.coingecko.com/api/v3/simple/price"
            params = {"ids": "solana", "vs_currencies": "usd"}
            async with s.get(url, params=params, timeout=aiohttp.ClientTimeout(total=5)) as r:
                if r.status == 200:
                    data = await r.json()
                    if "solana" in data:
                        return float(data["solana"]["usd"])
    except Exception:
        pass

    try:
        async with aiohttp.ClientSession() as s:
            url = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
            async with s.get(url, timeout=aiohttp.ClientTimeout(total=5)) as r:
                if r.status == 200:
                    data = await r.json()
                    return float(data["price"])
    except Exception:
        pass

    try:
        async with aiohttp.ClientSession() as s:
            url = "https://api.coinpaprika.com/v1/tickers/sol-solana"
            async with s.get(url, timeout=aiohttp.ClientTimeout(total=5)) as r:
                if r.status == 200:
                    data = await r.json()
                    return float(data["quotes"]["USD"]["price"])
    except Exception:
        pass

    return 0.0  # All APIs failed
