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
    characteristics_link = None
    for link in Links.objects.values_list('link', flat=True):
        try:
            response = uri(link)
            soup = BS(response.content, 'html.parser')
            handler = soup.find('div', class_='product__heading').find('h1', class_='product__title').text
            price = int(soup.find('div', class_='product-price__wrap ng-star-inserted').find('p', class_='product-price__big').text.replace('₴', ''))
            amount_feedback = soup.find('ul', class_='tabs__list').find_all('li', class_='tabs__item ng-star-inserted')[2].text.replace('Відгуки', '')
            characteristics_link = soup.find('ul', class_='tabs__list').find_all('li', class_='tabs__item ng-star-inserted')[1].findNext('a')['href']
        except:
            price = None
            pass

        if characteristics_link is not None:
            try:
                response_for_characteristics = uri(characteristics_link)
                soup_for_characteristics = BS(response_for_characteristics.content, 'html.parser')
                characteristics_items = soup_for_characteristics.find_all('div', class_='characteristics-full__item ng-star-inserted')
                color = 'None'
                material = 'None'
                brand = 'None'
                series = 'None'
                guarantee = 'None'
                for item in characteristics_items:
                    label = item.find('dt', class_='characteristics-full__label').find('span').text
                    value = item.find('dd', class_='characteristics-full__value').text
                    if label == 'Сумісний бренд':
                        brand = value
                    elif label == 'Гарантія':
                        guarantee = value
                    elif label == 'Колір':
                        color = value
                    elif label == 'Матеріал':
                        material = value
                    elif label == 'Серія':
                        series = value

                bd_for_info = Info(
                    product_name=handler,
                    price=price,
                    reviews=amount_feedback,
                    color=color,
                    material=material,
                    brand=brand,
                    series=series,
                    guarantee=guarantee
                )
                bd_for_info.save()
                time.sleep(0.03)
            except Exception as ex:
                print(ex)

    print("Парсинг окончен!")


if __name__ == '__main__':
    scrape_data()
