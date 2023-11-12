from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from models import session, Pistols
import requests
import json

ua = UserAgent()

type_cs = {
    "Ножи": 2, "Перчатки": 13, "Пистолеты": 5, "Пистолеты-пулеметы": 6, "Штурмовые винтовки": 3,
    "Снайперские винтовки": 4,
    "Дробовики": 7, "Пулеметы": 8, "Ключи": 1, "Другие": "10&type=12&type=14&type=11&type=9&type=18&type=19"
}


def get_currency_rate():
    """
    Getting the dollar rate
    :return: course rub.
    """
    url = "https://www.google.com/search?q=курс+доллара+к+рублю"
    response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    soup = BeautifulSoup(response.content, "html.parser")
    convert = soup.find(
        'span', {'class': 'DFlfde SwHCTb', 'data-precision': '2'}
    )
    return float(convert.text.replace(',', '.'))


def cs_money_add(type_data, user_id, table):
    """
    Add skins cs go from CSGOMONEY in BD
    """
    item = 60
    count = 0
    course_rub = get_currency_rate()

    while True:

        url = f'https://cs.money/1.0/market/sell-orders?limit=60&maxPrice=43.2198012902645&' \
              f'minPrice=1.0804388915647758&offset={item}&order=desc&sort=discount&type={type_data}'
        response = requests.get(
            url=url,
            headers={'user-agent': f'{ua.random}'}
        )

        if response.status_code != 200:
            break

        item += 60
        data = response.json()
        items = data.get('items')
        if items is not None and len(items) == 60:
            for simple in items:
                if simple["pricing"].get("discount") is not None and simple["pricing"].get("discount") >= 0.20:
                    new_skins = table(
                        request_user_id=user_id, full_name=simple["asset"]["names"]["full"],
                        url=simple["links"].get('3d'),
                        BeforePrice=round(simple["pricing"].get('priceBeforeDiscount') * course_rub, 1),
                        PriceNow=round(simple["pricing"].get('computed') * course_rub, 1),
                        Discount=round(simple["pricing"]["discount"] * 100, 1),
                        from_site="CSGOMONEY"
                    )
                    session.add(new_skins)
                    session.commit()
            count += 1

# def steam_data(type_data=2):
#     """
#     Getting json file with the necessary parameters and discounts
#     :param type_data: parametrs steam skins
#     :return: json result in 'result.json'
#     """
#     item = 60
#     result = []
#     count = 0
#     course_rub = get_currency_rate()
#
#     while True:
#
#         url = f'https://cs.money/1.0/market/sell-orders?limit=60&maxPrice=43.2198012902645&' \
#               f'minPrice=1.0804388915647758&offset={item}&order=desc&sort=discount&type={type_data}'
#         response = requests.get(
#             url=url,
#             headers={'user-agent': f'{ua.random}'}
#         )
#
#         if response.status_code != 200:
#             break
#
#         item += 60
#         data = response.json()
#         items = data.get('items')
#         if items is not None and len(items) == 60:
#             for simple in items:
#                 if simple["pricing"].get("discount") is not None and simple["pricing"].get("discount") >= 0.20:
#                     item_full_name = simple["asset"]["names"]["full"]
#                     item_3d = simple["links"].get('3d')
#                     item_price = simple["pricing"].get('priceBeforeDiscount') * course_rub
#                     item_price_now = simple["pricing"].get('computed') * course_rub
#                     item_discount = simple["pricing"]["discount"] * 100
#
#                     result.append(
#                         {
#                             'full_name': item_full_name,
#                             '3d': item_3d,
#                             'BeforePrice': round(item_price, 1),
#                             'PriceNow': round(item_price_now, 1),
#                             'Discount': round(item_discount, 1),
#                         }
#                     )
#             count += 1
#
#     with open('result.json', 'w') as file:
#         json.dump(result, file, indent=4, ensure_ascii=False)


# Добавление в БД


