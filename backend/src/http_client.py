from aiohttp import ClientSession
from async_lru import alru_cache

class HttpClient:
    def __init__(self, base_url: str, api_key: str):
        self.session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )

# pro-api.coinmarketcap.com
        
class CMCHttpClient(HttpClient):
    @alru_cache
    async def get_listings(self):
        async with self.session.get("/v1/cryptocurrency/listings/latest") as res:
            result = await res.json()
            return result["data"]
        
    @alru_cache
    async def get_cyrrency(self, currency_id: int):
        async with self.session.get("/v2/cryptocurrency/quotes/latest",
                                     params={"id": currency_id}) as res:
            result = await res.json()
            return result["data"][str(currency_id)]