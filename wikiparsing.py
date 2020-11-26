import requests
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/w/index.php"
a = ord("а")
LETTERS = {chr(i).upper(): 0 for i in range(a, a + 32)}


for letter in LETTERS:
    params = {"title": "Категория:Животные_по_алфавиту", "from": letter}

    while True:
        response = requests.get(URL, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        animal_block = soup.find("div", class_="mw-category-group")
        animals = animal_block.text.split("\n")

        if animals[0] != letter:
            break

        LETTERS[letter] += len(animals) - 1

        params = {
            "title": "Категория:Животные_по_алфавиту",
            "pagefrom": animals[-1],
        }

        if len(animals) < 201:
            break

for key, value in LETTERS.items():
    print(f"{key}: {value}")
