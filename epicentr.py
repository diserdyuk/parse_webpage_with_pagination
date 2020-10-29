import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):    # функ.получает код html по url из функ.main
    r = requests.get(url)    # объект response 
    if r.ok: # уловка, что-бы сайт не забанил парсер, ok это ответ 200=True, при 403, 404 и др.=False
        return r.text
    print(r.status_code)


def write_csv(d):    # функц.записывает спарс.данные в csv
    with open('epicentr_phones.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow((d['name'],
                        d['price'],
                        d['url']))


def clear_data(s):    # функц.удаляет все лишние данные кроме цифр
    # Цена: 3 599 грн
    s = s.split()[1:-1]
    return ''.join(s)
    

def get_page(html):    # функция собрала карточки телефонов на странице
    soup = BeautifulSoup(html, 'lxml')
    
    cards = soup.find_all('div', class_ = 'columns product-Wrap card-wrapper')
    
    cnt = 0
    for card in cards:
        cnt += 1    # для отслеживания кол-ва спарсенных данных

        try:    # есил инфо.нет, исключение ловится
            name = card.find('b', class_='nc').text
        except:
            name = ''

        try:
            prices = card.find('p', class_='card__price-actual').get('title')
            # price_data_clear = price.replace('Цена:', '').replace('грн', '').replace(' ', '')    # 2й вар.очистки данных
            price = clear_data(prices)
        except:
            prices = ''

        try:
            url = 'https://epicentrk.ua' + card.find('a', class_='custom-link custom-link--big custom-link--inverted custom-link--blue').get('href')
        except:
            url = ''


        data = {'name': name,    # словарь, в которы собираются все спарсенные данные
                'price': price,
                'url': url}

        write_csv(data)    # функц.записывает данные в csv



# pages
# 1 https://epicentrk.ua/shop/smartfony-i-mobilnye-telefony/?PAGEN_1=1
# 4 https://epicentrk.ua/shop/smartfony-i-mobilnye-telefony/?PAGEN_1=4



def main():    # фукц.в которой собираются др.функции
    url = 'https://epicentrk.ua/shop/smartfony-i-mobilnye-telefony/?PAGEN_1={}'    # новая ссылка, для парсинга послед.страниц
    
    for i in range(1, 6):    # цикл генерит цифры от 1 до 6
        url_pattern = url.format(str(i))    # цифры подставл.через метод format
        get_page(get_html(url_pattern))


if __name__ == '__main__':    # точка входа
    main()
