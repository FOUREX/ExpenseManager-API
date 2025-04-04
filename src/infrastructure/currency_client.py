from typing import Protocol

from aiohttp import ClientSession
from bs4 import BeautifulSoup


class CurrencyClient(Protocol):
    async def get_usd_to_uah(self) -> str:
        raise NotImplementedError()


class CurrencyClientImpl(CurrencyClient):
    """
    На мою думку, парсинг сторінки не є оптимальним. Тому заразом реалізую отримання курсу через стороннє API.
    Метод отримання курсу можна змінити за допомогою змінної нижче (USE_API)

    Методи повертають строкові значення, бо вони ж і використовуються в підрахунках через Decimal для запобігання
    потенційних помилок

    Використовується відкрите API дані якого оновлюються раз у 24 години, тому можуть бути розбіжності. Можливе
    досягнення RateLimit, тому передбачено парсинг зі сторінки у крайнему разі
    """

    USE_API: bool = False

    def __init__(
            self,
            parse_url: str | None = "https://wise.com/gb/currency-converter/usd-to-uah-rate?amount=1",
            api_url: str | None = "https://open.er-api.com/v6/latest/USD"  # Дані оновлюються раз у 24 години
    ):
        self.parse_url = parse_url
        self.api_url = api_url

    async def _parse_from_page(self) -> str:
        async with ClientSession() as session:
            async with session.get(self.parse_url) as response:
                page_text = await response.text()

        soup = BeautifulSoup(page_text, "html.parser")
        result = soup.find("span", attrs={"class": "text-success"}).text

        return result

    async def _get_from_api(self) -> str:
        async with ClientSession() as session:
            async with session.get(self.api_url) as response:
                status = response.status

                if status != 200:
                    print("Не вдалося отримати дані з API! Парсинг сторінки...")
                    return await self._parse_from_page()

                json = await response.json()

        return str(json["rates"]["UAH"])

    async def get_usd_to_uah(self) -> str:
        return await self._get_from_api() if self.USE_API else await self._parse_from_page()


async def main():
    currency_client = CurrencyClientImpl()
    currency = await currency_client.get_usd_to_uah()

    print(currency)


if __name__ == "__main__":
    from asyncio import new_event_loop

    loop = new_event_loop()
    loop.run_until_complete(main())
