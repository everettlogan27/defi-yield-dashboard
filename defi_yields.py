import requests

API_URL = "https://yields.llama.fi/pools"

def fetch_defi_yields(limit=10):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        pools = data.get("data", [])

        print(f"\n📈 Топ {limit} DeFi пулов по доходности:\n")
        for pool in sorted(pools, key=lambda x: x.get("apy", 0), reverse=True)[:limit]:
            name = pool.get("project", "Unknown")
            symbol = pool.get("symbol", "N/A")
            apy = pool.get("apy", 0)
            chain = pool.get("chain", "N/A")
            print(f"🔹 {name} ({symbol}) на {chain} → APY: {apy:.2f}%")

    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")

if __name__ == "__main__":
    fetch_defi_yields()
