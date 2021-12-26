import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import product


if __name__ == '__main__':
    years = ['2020', '2021']
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09'] + [str(x) for x in range(10, 29)]
    base_url = 'https://www.anekdot.ru/release/anekdot/day/'

    jokes = []
    for (year, month, day) in product(years, months, days):
        if day == '01':
            print(f'{year}.{month}...')

        url = base_url + year + '-' + month + '-' + day + '/'
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")
        search_result = soup.find_all('div', class_='topicbox')

        for box in search_result:
            text = box.findAll('div', class_='text')
            if len(text):
                jokes.append(text[0].get_text().replace('\r', ' ').replace('\xad', ' '))

    print(f'Number of jokes: {len(jokes)}')

    df = pd.DataFrame({'Jokes': jokes})
    df.to_csv('jokes.csv', index=False)
