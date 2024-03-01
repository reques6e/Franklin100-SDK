import aiohttp

class FranklinAPI:
    def __init__(self, key):
        self.base_url = 'https://franklin100.ru/api/v2'
        self.params = {'key': key}
        self.session = aiohttp.ClientSession()

    async def get_services(self):
        endpoint = 'services'
        response = await self.send_request(endpoint)
        return await response.json()

    async def create_order(self, service_id, link, quantity):
        endpoint = 'add'
        params = {'service': service_id, 'link': link, 'quantity': quantity}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def get_order_status(self, order_id):
        endpoint = 'status'
        params = {'order': order_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def get_orders_status(self, order_ids):
        endpoint = 'status'
        params = {'orders': ','.join(map(str, order_ids))}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def create_refill(self, order_id):
        endpoint = 'refill'
        params = {'order': order_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def get_balance(self):
        endpoint = 'balance'
        response = await self.send_request(endpoint)
        return await response.json()

    async def cancel_order(self, order_id):
        endpoint = 'cancel'
        params = {'order': order_id}
        response = await self.send_request(endpoint, params=params)
        return await response.json()

    async def send_request(self, endpoint, params=None):
        url = f'{self.base_url}?action={endpoint}'
        async with self.session.get(url, params=params) as response:
            return response
