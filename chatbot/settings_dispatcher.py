from pprint import pprint
import random
import datetime

GROUP_ID=198507410
TOKEN = 'a8fb6d94efec9852f7287f73067ecb502eb57a55675b0cb6a53295e1f8a0892e9739126335f98f0ee514c'

CITY = {"Гонконг", "Бангкок", "Макао",
        "Сингапур", "Сингапур", "Париж",
        "Дубай", "Дели", "Стамбул",
        "Куала-Лумпур", "Москва", "Питер"}


DATE = []
date_now = datetime.datetime.now().date()


date = date_now
while date != date_now + datetime.timedelta(weeks=1):

    number_of_flights = random.randint(180,300)
    for flight in range(number_of_flights):

        departure_time = random.randint(0,23)
        departure_city = random.choice(list(CITY))

        arrival_city = random.choice(list(CITY - set(departure_city)))


        fly_time = str(departure_time) + ".00"

        DATE.append({"departure_city" :departure_city, "arrival_city": arrival_city,
                     "date": date, "fly_time": fly_time, "flight number": random.randint(1000,9999),
                     "free places":random.randint(1, 5)})

    date += datetime.timedelta(days=1)
#pprint(DATE)


TEXT_HELP = '''
1.Ввод города отправления.
2.Ввод города назначения.
3.Ввод даты: спрашиваем у пользователя дату вылета в формате 01-05-2019.
4.Выбор рейса.
5.Предлагаем написать комментарий в произвольной форме.
6.Уточняем введенные данные. Пользователь должен ввести "да" или "нет".
7.Запрашиваем номер телефона.

Если во время сценария вводится команда (/ticket или /help), то сценарий останавливается и выполняется команда 

'''

INTENTS = [

    {
        "name": 'Справка о том, как работает робот.',
        "tokens": r"/help",
        "scenario": None,
        "answer": TEXT_HELP

    },
    {
        "name": 'начинает сценарий заказа билетов',
        "tokens": r"/ticket",
        "scenario": "registration",
        "answer": None

    },
]


SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "steps":{
            "step1": {
                "text": "Город отправления принят '{departure_city}'. Введите город назначения.",
                "failure_text": "Город отправления должен состоять из 3-10 букв. Попробуйте еще раз",
                "handler": "handler_departure_city",
                "next_step": "step2"
            },
            "step2": {
                "text": " Город назначения принят '{arrival_city}'. Введите дату отправления.",
                "failure_text": "Город назначения должен состоять из 3-10 букв. Попробуйте еще раз",
                "handler": "handler_arrival_city",
                "next_step": "step3"
            },
            "step3": {
                "text": " Будем искать билеты на '{date}'.\n",
                "failure_text": "Дата ерор",
                "handler": "handler_date",
                "next_step": "step4"
            },
            "step4": {
                "text": " Выбор рейса {flight}.\n Предлагаем написать комментарий в произвольной форме.",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще раз",
                "handler": "handler_flight_selection",
                "next_step": "step5"
            },

            "step5": {
                "text": " Предлагаем написать комментарий в произвольной форме.",
                "failure_text": "Eror comment",
                "handler": "handler_comment",
                "next_step": "step6"
            },

            "step6": {
                "text": "  Уточняем введенные данные. {departure_city} --> {arrival_city} {date} рейс {flight} {comment}",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще раз",
                "handler": "handler_true",
                "next_step": "step7"
            },

            "step7": {
                "text": "Запрашиваем номер телефона.",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще раз",
                "handler": "handler_date",
                "next_step": "step8"
            },
            "step8": {
                "text": "Спасибо за регистрацию, {name}! Мы отправим на {email} билет, распечатайте его.",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
        }
    }

}
