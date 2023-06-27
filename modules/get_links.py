from load_django import load
import requests

load()

from parser_app.models import Keywords, Links

all_keys = Keywords.objects.values('name')
sort_keys = []
for i in range(len(all_keys)):
    sort_keys.append((all_keys[i].get('name')).replace(' ', '+'))

for u in range(len(sort_keys)):
    try:
        url = f'https://search.rozetka.com.ua/search/api/v6/?front-type=xl&country=UA&lang=ru&page=1&text={sort_keys[u]}&seller=rozetka'
        response = requests.get(url)
        data = response.json()
        page_count = int(data['data']['pagination']['total_pages'])
        page_size = int(data['data']['pagination']['page_size'])
        for i in range(page_count):
            response_for_href = requests.get(f'https://search.rozetka.com.ua/search/api/v6/?front-type=xl&country=UA&lang=ru&page={i + 1}&text={sort_keys[u]}&seller=rozetka')
            data_for_href = response_for_href.json()
            for j in range(page_size):
                get_title = data_for_href['data']['goods'][j]['title']
                print(get_title)
                get_link = data_for_href['data']['goods'][j]['href']
                print(get_link)
                bd_for_link = Links(name=get_title, link=get_link, status=True)
                bd_for_link.save()
    except:
        pass
