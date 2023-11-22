from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from models import session, ORM_MODEL_CLS
import requests
import logging
import os

ua = UserAgent()

if not os.path.isdir("logs"):
    os.mkdir("logs")


pars_logger = logging.getLogger(__name__)
pars_logger.setLevel(logging.INFO)

pars_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
pars_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

pars_handler.setFormatter(pars_formatter)
pars_logger.addHandler(pars_handler)

type_cs = {
    "пистолеты": 5, "пистолеты-пулеметы": 6, "штурмовые винтовки": 3,
    "снайперские винтовки": 4, "дробовики": 7, "пулеметы": 8, "ключи": 1,
    "другое": "10&type=12&type=14&type=11&type=9&type=18&type=19"
}


def get_currency_rate():
    """
    Getting the dollar rate
    :return: course rub type float.
    """
    url = "https://www.google.com/search?q=курс+доллара+к+рублю"
    response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})
    pars_logger.info(f"Function get_currency_rate response status code: {response.status_code}")
    soup = BeautifulSoup(response.content, "html.parser")
    convert = soup.find(
        'span', {'class': 'DFlfde SwHCTb', 'data-precision': '2'}
    )
    return float(convert.text.replace(',', '.'))


def cs_money_add(type_data: int, user_id: int, models: ORM_MODEL_CLS):
    """
    Add skins cs go from CSGOMONEY in DB
    param:
    type_data - type guns skins from CSGOMONEY
    user_id - ID user from models User
    table - guns models from DB
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

        pars_logger.info(f"From user - {user_id} cs_money_add requests status code: {response.status_code}, "
                         f"item: {item}, type_data: {type_data}")
        item += 60
        data = response.json()
        items = data.get('items')
        if items is not None and len(items) == 60:
            for simple in items:
                if simple["pricing"].get("discount") is not None and simple["pricing"].get("discount") >= 0.20:
                    if simple["links"].get('3d') is not None:
                        new_skins = models(
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
    pars_logger.info(f"Add {count} new skins in DB {models.__tablename__}")



