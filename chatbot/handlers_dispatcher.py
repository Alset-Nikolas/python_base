
"""
Handler - функция, которая принимает на вход text (такст входящего сообщения) и context (dict), а возвращает bool:
True если шаг пройден, False если данные введены неправильно.
"""
import re
re_departure_city = re.compile(r'^[\w\-\s]{3,40}$')
re_arrival_city = re.compile(r'^[\w\-\s]{3,40}$')
re_date = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")
re_flight = re.compile(r"\d{4}")
def handler_departure_city(text, context):
    match = re.match(re_departure_city, text)
    if match:
        context["departure_city"] = text
        return True
    else:
        return False


def handler_arrival_city(text, context):
    match = re.match(re_arrival_city, text)
    if match:
        context["arrival_city"] = text
        return True
    else:
        return False

def handler_date(text, context):
    match = re.match(re_date, text)
    if match:
        context["date"] = text
        return True
    else:
        return False

def handler_true(text, context):
    return True

def handler_flight_selection(text, context):
    match = re.match(re_flight, text)
    if match:
        context["flight"] = text
        return True
    else:
        return False

def handler_comment(text, context):
    context["comment"] = text
    return True