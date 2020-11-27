# wikipedia_parsing

### Скрипт, позволяющий получить из википедии список всех животных на русском языке и вывести количество животных на каждую букву алфавита. 

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Запуск проекта (на примере Linux)

Перед тем, как начать: если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

- Создайте на своем компютере папку проекта foodgram `mkdir wikipedia_parsing` и перейдите в нее `cd wikipedia_parsing`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/SergePogorelov/wikipedia_parsing .`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Запустите скрипт `python wikiparsing.py`

**Результы работы скрипта будут выведены в консоль**
```
А: 1077
Б: 1485
В: 488
Г: 929
Д: 705
Е: 100
Ж: 378
З: 579
И: 321
Й: 3
К: 2058
Л: 660
М: 1172
Н: 429
О: 726
П: 1629
Р: 524
С: 1652
Т: 907
У: 228
Ф: 168
Х: 254
Ц: 203
Ч: 622
Ш: 255
Щ: 142
Ъ: 0
Ы: 0
Ь: 0
Э: 192
Ю: 123
Я: 190

```

## В разработке использованы

- [Python](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [threading](https://docs.python.org/3/library/threading.html)

