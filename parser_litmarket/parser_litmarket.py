import requests
from bs4 import BeautifulSoup as BS

URL = 'https://vse-chasti-filmov.pro'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_data(html):
    bs = BS(html, 'html.parser')
    items = bs.find_all('div', class_='th-item')
    market_list = []
    for item in items:
        title = item.get_text(strip=True)
        href = item.find('a').get('href')
        market_list.append(
            {
                'title': title,
                'href': href,
            }
        )
    return market_list


def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        market_list = []
        for page in range(1, 5):
            html_content = get_html(URL, params={'page': page}).text
            market_list.extend(get_data(html_content))
        return market_list
    else:
        raise Exception('Error parsing page')


# films = parsing()
# for film in films:
#     print(film)
