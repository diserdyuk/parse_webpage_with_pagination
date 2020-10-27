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


def get_page(html):
    soup = BeautifulSoup(html, 'lxml')
    colums = soup.find_all('div', class_ = 'columns product-Wrap card-wrapper')
    print(len(colums))




def main():    # фукц.в которой собираются др.функции
    url = 'https://epicentrk.ua/shop/smartfony-i-mobilnye-telefony/'
    get_page(get_html(url))


if __name__ == '__main__':    # точка входа
    main()
