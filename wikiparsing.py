import threading

import requests
from bs4 import BeautifulSoup


URL = "https://ru.wikipedia.org/w/index.php"
a = ord("а")
LETTERS = {chr(i).upper(): 0 for i in range(a, a + 32)}


def count_animals(letter):
    params = {"title": "Категория:Животные_по_алфавиту", "from": letter}

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
            return

        LETTERS[letter] += len(animals) - 1

        if len(animals) < 201:
            return

        params = {
            "title": "Категория:Животные_по_алфавиту",
            "pagefrom": animals[-1],
        }


def wait_until_threadings_finished():
    for t in threading.enumerate()[1:]:
        t.join()


def print_result():
    for k, v in LETTERS.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    for letter in LETTERS:
        thread = threading.Thread(target=count_animals, args=(letter,))
        thread.start()

    wait_until_threadings_finished()
    print_result()
