from collections import defaultdict, Counter
import requests

from bs4 import BeautifulSoup

URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"


def get_page(url):
    try:
        page = requests.get(url).text
        return page
    except ConnectionError:
        print('Ошибка соединения')


def get_animals(url=URL):
    alphabet = Counter()
    page = get_page(url)
    exclude = ('Следующая страница', 'Предыдущая страница')
    while True:
        soup = BeautifulSoup(page, 'html.parser')
        links = soup.find('div', id='mw-pages').find_all('a')
        for name in links:
            if name.text in exclude:
                continue
            if name.text == 'Aaaaba':
                return alphabet
            alphabet.update(name.text[0])
        for link in links:
            if link.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + link.get('href')
                page = get_page(url)


if __name__ == '__main__':
    lst = list(get_animals().items())
    lst.sort(key=lambda x: x[0])
    for letter, value in lst:
        print(f'{letter}: {value}')
