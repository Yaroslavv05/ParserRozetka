import time
from load_django import load
import requests
from bs4 import BeautifulSoup as BS

load()

from parser_app.models import Links, Info


def uri(link):
    response = requests.get(link)
    return response


def scrape_data():
    all_links = Links.objects.values_list('link', flat=True)
    characteristics = []

    for link in all_links:
        try:
            response = uri(link)
            soup = BS(response.content, 'html.parser')
            handler = soup.find('div', class_='product__heading').find('h1', class_='product__title').text
            price = int(soup.find('div', class_='product-price__wrap ng-star-inserted').find('p', class_='product-price__big').text.replace('₴', ''))
            amount_feedback = soup.find('ul', class_='tabs__list').find_all('li', class_='tabs__item ng-star-inserted')[2].text.replace('Відгуки', '')
            characteristics_link = soup.find('ul', class_='tabs__list').find_all('li', class_='tabs__item ng-star-inserted')[1].findNext('a')['href']
        except:
            continue

        if characteristics_link:
            try:
                response_for_characteristics = uri(characteristics_link)
                soup_for_characteristics = BS(response_for_characteristics.content, 'html.parser')
                current_characteristics = []
                characteristics_items = soup_for_characteristics.find('dl', class_='characteristics-full__list').find_all('div', class_='characteristics-full__item ng-star-inserted')[:5]
                for item in characteristics_items:
                    try:
                        label = item.findNext('span').text
                        value = item.findNext('a', class_='ng-star-inserted').text
                        characteristic = f'{label} - {value}'
                    except:
                        continue
                    current_characteristics.append(characteristic)
                characteristics.append(current_characteristics)

                bd_for_info = Info(
                    product_name=handler,
                    price=price,
                    reviews=amount_feedback,
                    characteristic1=current_characteristics[0] if len(current_characteristics) > 0 else None,
                    characteristic2=current_characteristics[1] if len(current_characteristics) > 1 else None,
                    characteristic3=current_characteristics[2] if len(current_characteristics) > 2 else None,
                    characteristic4=current_characteristics[3] if len(current_characteristics) > 3 else None,
                    characteristic5=current_characteristics[4] if len(current_characteristics) > 4 else None
                )
                bd_for_info.save()
                time.sleep(0.03)
            except:
                continue

    print("Парсинг окончен!")


if __name__ == '__main__':
    scrape_data()
