GROUP_ID=198507410
TOKEN = 'a8fb6d94efec9852f7287f73067ecb502eb57a55675b0cb6a53295e1f8a0892e9739126335f98f0ee514c'

INTENTS = [
    {
        "name": 'Дата проведения',
        "tokens": ("когда", "сколько", "дата", "дату"),
        "scenario": None,
        "answer": "Конференция проводится 15го апреля, регистрация в 10 утра"

    },
    {
        "name": 'Место проведения',
        "tokens": ("где", "место", "локация", "адрес", "метро"),
        "scenario": None,
        "answer": "Конференция проводится в павильоне 18Г Экспоцентре"

    },
    {
        "name": 'Регистрация',
        "tokens": ("регист", "добав"),
        "scenario": "registration",
        "answer": None

    }
]

SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Чтобы зарегистрироваться, введите ваше имя. Оно будет написано на бэйджике",
                "failure_text": "Имя должно состоять из 3-10 букв и дефиса. Попробуйте еще раз",
                "handler": "handler_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "Введите email. Мы отправим на него все данные",
                "failure_text": "Во введенном адресе ошибка. Попробуйте еще раз",
                "handler": "handler_email",
                "next_step": "step3"
            },
            "step3": {
                "text": "Спасибо за регистрацию, {name}! Мы отправим на {email} билет, распечатайте его.",
                "image": "handler_generate_ticket",
                "failure_text": None,
                "handler": None,
                "next_step": None
            },
        }
    }

}

DEFAULT_ANSWER = "Не знаю как на это ответить." \
                 "Могу сказать когда и где пройдет конференция, а также зарегистрировать вас. Просто спросите"

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='81k',
    host='localhost',
    database='vk_chat_bot'
)
