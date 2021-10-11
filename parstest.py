from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from openpyxl.workbook import Workbook

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
URL = 'https://auto.ru/'


def pars_all_cars_names(url, headers):
    """Данная функция парсит самые популярные марки машин с сайта Авто ру"""
    response = requests.get(url, headers)
    html = bs(response.content, 'html.parser')
    names = html.findAll('a', class_='IndexMarks__item')
    cars_name_list = []
    n = 0
    for name in names:
        n += 1
        cars_name_list.append(name.find('div', class_='IndexMarks__item-name').get_text())
    return cars_name_list


cars_name_list = pars_all_cars_names(url=URL, headers=HEADERS)


def choose_your_cars(cars_name_list):
    """"Обычный запрос марки у пользователя"""
    n = 0
    for inames in cars_name_list:
        n += 1
        print(f'{n} : {inames}')
    while True:
        try:
            choose_mark = int(input('Выберите номер марки: '))
            if choose_mark > n:
                print("Введите верное значение")
            else:
                return cars_name_list[choose_mark - 1]
        except:
            print("Неверный ввод")


selected_cars_name = choose_your_cars(cars_name_list)


def rework_url(selected_cars_name):
    """Функция меняет названия российских авто на соответствующие url на сайте"""
    if selected_cars_name == 'УАЗ':
        return 'uaz'
    if selected_cars_name == 'ГАЗ':
        return 'gaz'
    if selected_cars_name == 'LADA (ВАЗ)':
        return 'vaz'
    else:
        return selected_cars_name

cars_name = rework_url(selected_cars_name)
URL_2 = f'https://auto.ru/cars/{cars_name}/all/'


def pars_autos(url, headers):
    response = requests.get(url, headers)
    html = bs(response.content, 'html.parser')
    advertisement = html.findAll('div', class_='ListingItem')
    data_list = []
    n = 0
    for car in advertisement:
        n += 1
        title = car.find('a', class_='Link ListingItemTitle__link').get_text()
        link = car.find('a', class_='Link ListingItemTitle__link').get('href')
        try:
            price = car.find('div', class_='ListingItemPrice__content').get_text()
            data_list.append({
                'Название авто': title,
                'Ссылка': link,
                'Цена': price
            })
        except AttributeError:
            pass
    return data_list


def rework_price(data_list):
    """Убираем не нужное из цены, что бы удобнее было работать с базой данных"""
    new_data = {}
    big_data = []
    for i in data_list:
        for key, value in i.items():
            remove_space = value.replace(u'\xa0', u'')
            remove_rub = remove_space.replace('₽', '')
            remove_word = remove_rub.replace('от ', '')
            if key == 'Цена':
                new_data[key] = int(remove_word)
            else:
                new_data[key] = remove_word
        big_data.append(new_data)
        new_data = {}
    return big_data


def full_pars():
    big_data = []
    first_page = pars_autos(url=URL_2, headers=HEADERS)
    big_data.extend(first_page)
    n = 1
    while True:
        n += 1
        new_url = f'https://auto.ru/cars/{cars_name}/all/?page={n}'
        info = pars_autos(url=new_url, headers=HEADERS)
        if len(info) == 0:
            break
        big_data.extend(info)
    return big_data


def rework_and_save():
    a = rework_price(full_pars())
    save_file = pd.DataFrame(a)
    save_file.to_excel('./pars_result.xlsx')


rework_and_save()
