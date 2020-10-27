import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # функ.получает код html по url из функ.main
    r = requests.get(url)    # объект response 
    if r.ok: # уловка, что-бы сайт не забанил парсер, ok это ответ 200=True, при 403, 404 и др.=False
        return r.text
    print(r.status_code)


def write_csv(d):
    with open('epicentr_phones.csv', 'a') as f:
        write = csv.writer(f)
        pass


def get_page(html):    # функция собрала карточки телефонов на странице
    soup = BeautifulSoup(html, 'lxml')
    
    cards = soup.find_all('div', class_ = 'columns product-Wrap card-wrapper')
    
    cnt = 0
    for card in cards:
        cnt += 1

        try:    # есил инфо.нет, исключение ловится
            name = card.find('b', class_='nc').text
        except:
            name = ''

        try:
            price = card.find('p', class_='card__price-actual').get('title')
            price_data_clear = price.replace('Цена:', '').replace('грн', '').replace(' ', '')
        except:
            price = ''

        try:
            url = 'https://epicentrk.ua' + card.find('a', class_='custom-link custom-link--big custom-link--inverted custom-link--blue').get('href')
        except:
            url = ''
        print(cnt, url)

        




def main():    # фукц.в которой собираются др.функции
    url = 'https://epicentrk.ua/shop/smartfony-i-mobilnye-telefony/'
    get_page(get_html(url))


if __name__ == '__main__':    # точка входа
    main()
