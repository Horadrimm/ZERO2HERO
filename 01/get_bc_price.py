import requests
import json
import btc_calc
import get_data_by_url

from some_module import print_hello




# Контроллер
if __name__ == "__main__":
    # Параметры запуска программы
    # Приходят из вне, командная строка, http, конфигурация
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    currencys_list = ['USD','EUR']
    btc_count      = 10

    # Получение данных из внешних источников
    # База данных, внешнее api, файлы
    bc_price = get_data_by_url.data_from_url(url)

    # Отладочная информация
    print('На',bc_price['time']['updated'])

    # Бизнес логика
    for currency in currencys_list:
        code = bc_price['bpi'][currency]['code']
        rate = bc_price['bpi'][currency]['rate']
        
        # Подготовка данных для корневой логики
        rate_to_float = float(rate.replace(',',''))
        
        # Ядро программы
        btc_math = btc_calc.btc_math(rate_to_float,btc_count)

        # Слой представления данных
        # print, http ответ, любой ответ для клиента
        print(f'Цена {btc_count} BitCoin в {code} стоит {btc_math}')


# my_super_dict = {
#     "USD" : 70,
#     "EUR" : 72,
# }

# rubs = 100
# white_list_currency = ["USD", "EUR"]

# result_dict = {}
# # Перевести валюту  в рубли
# for i in white_list_currency:
#     result = rubs / my_super_dict[i]
#     result_dict[i] =  result

# print(result_dict)
# # Метод dict.get( key, default )