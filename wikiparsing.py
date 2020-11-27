import requests
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/w/index.php"
a = ord("а")
LETTERS = {chr(i).upper(): 0 for i in range(a, a + 32)}


def get_count_for_letter(letter):
    params = {"title": "Категория:Животные_по_алфавиту", "from": letter}
    count = 0

    while True:
        session = requests.Session()
        response = session.get(URL, params=params)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for the letter '{letter}': {http_err}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        animal_block = soup.find("div", class_="mw-category-group")
        animals = animal_block.text.split("\n")

        if animals[0] != letter:
            return count

        count += len(animals) - 1

        if len(animals) < 201:
            return count

        params = {
            "title": "Категория:Животные_по_алфавиту",
            "pagefrom": animals[-1],
        }


if __name__ == "__main__":
    for letter in LETTERS:
        count = get_count_for_letter(letter)
        LETTERS[letter] = count
        print(f"{letter}: {count}")
