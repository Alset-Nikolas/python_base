from pprint import pprint
import random
import datetime

GROUP_ID = 198507410
TOKEN = 'a8fb6d94efec9852f7287f73067ecb502eb57a55675b0cb6a53295e1f8a0892e9739126335f98f0ee514c'

CITY = {"Гонконг", "Бангкок", "Макао",
        "Сингапур", "Сингапур", "Париж",
        "Дубай", "Дели", "Стамбул",
        "Куала-Лумпур", "Москва", "Санкт-Петербург"}

ALL_FLY_NUMBERS = set()


def create_DATEBASE():
    DATE = []
    date_now = datetime.datetime.now().date()

    date = date_now
    while date != date_now + datetime.timedelta(weeks=1):

        number_of_flights = random.randint(180, 300)
        for flight in range(number_of_flights):

            departure_time = random.randint(0, 23)
            departure_city = random.choice(list(CITY))

            arrival_city = random.choice(list(CITY - set(departure_city)))

            fly_time = str(departure_time) + ".00"
            while True:
                flight_number = random.randint(1000, 9999)
                if flight_number not in ALL_FLY_NUMBERS:
                    ALL_FLY_NUMBERS.add(flight_number)
                    break
            DATE.append({"departure_city": departure_city, "arrival_city": arrival_city,
                         "date": date, "fly_time": fly_time, "flight number": flight_number,
                         "free places": random.randint(1, 5)})

        date += datetime.timedelta(days=1)
    return DATE


DATE = create_DATEBASE()
TEXT_HELP = '''
==================================
Весь сценарий:
1.Ввод города отправления.
2.Ввод города назначения.
3.Ввод даты: спрашиваем у пользователя дату вылета в формате 01-05-2019.
4.Выбор рейса.
5.Предлагаем написать комментарий в произвольной форме.
6.Уточняем введенные данные. Пользователь должен ввести "да" или "нет".
7.Запрашиваем номер телефона.

Если во время сценария вводится команда (/ticket или /help), то сценарий останавливается и выполняется команда 
==================================
'''
INTENTS = [
    {
        "name": 'начинает сценарий заказа билетов',
        "tokens": r"/ticket",
        "scenario": "registration",
        "answer": None

    },
    {
        "name": 'Справка о том, как работает робот.',
        "tokens": r"/help",
        "scenario": None,
        "answer": TEXT_HELP

    },

]
SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Город отправления принят '{departure_city}'. Введите город назначения.",
                "failure_text": "У нас нет такого города в базе, попробуйте другие:\n {var}\n Введите город отправления:",
                "handler": "handler_departure_city",
                "next_step": "step2"
            },
            "step2": {
                "text": "Город назначения принят '{arrival_city}'. Введите дату отправления.",
                "failure_text": "У нас нет такого города в базе, попробуйте другие:\n {var}\n Введите город назначения:",
                "handler": "handler_arrival_city",
                "next_step": "step3"
            },
            "step3": {
                "text": "Будем искать билеты на '{date}'.\n",
                "failure_text": "Пример: 14-10-2020. В прошлое билет брать нельзя!",
                "handler": "handler_date",
                "next_step": "step4"
            },
            "step4": {
                "text": "Выбор рейса {flight}.\nПредлагаем написать комментарий в произвольной форме.",
                "failure_text": "Такого рейса нет в базе!",
                "handler": "handler_flight_selection",
                "next_step": "step5"
            },

            "step5": {
                "text": "Спасибо за комментарий! {comment}.\n Уточняем введенные данные.\n"
                        " {departure_city} --> {arrival_city} {date} рейс {flight}!\n да или нет?",
                "failure_text": "Такого рейса нет в базе!",
                "handler": "handler_comment",
                "next_step": "step6"
            },

            "step6": {
                "text": "Супер! Введите номер телефона",
                "failure_text": "да или нет",
                "handler": "handler_right",
                "next_step": "step7"
            },

            "step7": {
                "text": '''Мы будем звонить на {telephone}.
Спасибо за регистрацию!
Если хотите заказать еще один билет Введите город отправления:''',
                "failure_text": "Пример 89991112233",
                "handler": "handler_telephone",
                "next_step": None
            },

        }
    }

}
