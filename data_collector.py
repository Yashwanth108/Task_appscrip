import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_sector_data(sector):
    query = f"{sector} sector India market news"
    url = f"https://duckduckgo.com/html/?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            # Look for search result titles
            results = soup.find_all('a', class_='result__a')
            if not results:
                return "No data found"

            return "\n".join([r.get_text(strip=True) for r in results[:5]])