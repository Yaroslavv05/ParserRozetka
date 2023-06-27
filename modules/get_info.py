import time
from load_django import load
import requests
from bs4 import BeautifulSoup as BS

load()

from parser_app.models import Links, Info

all_link = Links.objects.values('link')
sort_link = []
for i in range(len(all_link)):
    sort_link.append((all_link[i].get('link')).replace(' ', '+'))


def uri(link):
    url = link
    response = requests.get(url)
    return response


characteristics_link = None
for i in range(len(sort_link)):
    try:
        soup = BS(uri(link=sort_link[i]).content, 'html.parser')
        handler = soup.find('div', attrs={'class': 'product__heading'}).find('h1', attrs={'class': 'product__title'}).text
        price = int(soup.find('div', attrs={'class': 'product-price__wrap ng-star-inserted'}).find('p', attrs={'class': 'product-price__big'}).text.replace('₴', ''))
        amount_feedback = soup.find('ul', attrs={'class': 'tabs__list'}).find_all('li', attrs={'tabs__item ng-star-inserted'})[2].text.replace('Відгуки', '')
        characteristics_link = soup.find('ul', attrs={'class': 'tabs__list'}).find_all('li', attrs={'tabs__item ng-star-inserted'})[1].findNext('a')['href']
    except:
        pass

    if characteristics_link is not None:
        soup_for_characteristics = BS(uri(link=characteristics_link).content, 'html.parser')
        for j in range(5):
            try:
                get_characteristics = soup_for_characteristics.find('dl', attrs={'class': 'characteristics-full__list'}).find_all('div', attrs={'class': 'characteristics-full__item ng-star-inserted'})[j]
                label = get_characteristics.findNext('span').text
                value = get_characteristics.findNext('a', attrs={'class': 'ng-star-inserted'}).text
                characteristic = f'{label} - {value}'
            except:
                try:
                    get_characteristics = soup_for_characteristics.find_all('section', attrs={'class': 'characteristics-full__group ng-star-inserted'})[j].findNext('dl', attrs={'class': 'characteristics-full__list'})
                    label = get_characteristics.findNext('span').text
                    value = get_characteristics.findNext('a', attrs={'class': 'ng-star-inserted'}).text
                    characteristic = f'{label} - {value}'
                except:
                    pass
            print(handler)
            print(price)
            print(amount_feedback)
            print(characteristics_link)
            print(characteristic)
            bd_for_info = Info(product_name=handler, price=price, reviews=amount_feedback, characteristic1=characteristic,
                               characteristic2=characteristic, characteristic3=characteristic,
                               characteristic4=characteristic, characteristic5=characteristic)
            bd_for_info.save()
            time.sleep(0.03)