import asyncio

import aiohttp
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/w/index.php"
a = ord("А")
LETTERS = {chr(i): 0 for i in range(a, a + 32)}


async def get_url_text(params, session):
    async with session.get(URL, params=params) as response:
        return await response.text()


async def count_animals(letter, session, params=None):
    if params is None:
        params = {"title": "Категория:Животные_по_алфавиту", "from": letter}
    
    text = await get_url_text(params, session)

    soup = BeautifulSoup(text, "html.parser")
    animal_block = soup.find("div", class_="mw-category-group")
    animals = animal_block.text.split("\n")

    if animals[0] != letter:
        return

    LETTERS[letter] += len(animals) - 1

    if len(animals) < 201:
        return

    params = {
        "title": "Категория:Животные_по_алфавиту",
        "pagefrom": animals[-1],
    }
    await count_animals(letter, session, params)


async def main():
    tasks  = []

    async with aiohttp.ClientSession() as session:
        for letter in LETTERS:
            task = asyncio.create_task(count_animals(letter, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


def print_result():
    for k, v in LETTERS.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    asyncio.run(main())
    print_result()
