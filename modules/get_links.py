from load_django import load
import requests

load()

from parser_app.models import Keywords, Links


def fetch_links(url):
    response = requests.get(url)
    data = response.json()
    goods = data['data']['goods']
    links = []
    for item in goods:
        title = item['title']
        link = item['href']
        links.append((title, link))
    return links


all_keys = Keywords.objects.values_list('name', flat=True)
sort_keys = [key.replace(' ', '+') for key in all_keys]

for keyword in sort_keys:
    try:
        url = f'https://search.rozetka.com.ua/search/api/v6/?front-type=xl&country=UA&lang=ru&page=1&text={keyword}&seller=rozetka'
        response = requests.get(url)
        data = response.json()
        page_count = int(data['data']['pagination']['total_pages'])
        page_size = int(data['data']['pagination']['page_size'])

        for page in range(1, page_count + 1):
            url = f'https://search.rozetka.com.ua/search/api/v6/?front-type=xl&country=UA&lang=ru&page={page}&text={keyword}&seller=rozetka'
            links = fetch_links(url)

            for title, link in links:
                bd_for_link = Links(name=title, link=link, status=True)
                bd_for_link.save()
    except:
        pass
print('Ссылки собраны!')