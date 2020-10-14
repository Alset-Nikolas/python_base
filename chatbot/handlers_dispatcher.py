
"""
Handler - функция, которая принимает на вход text (такст входящего сообщения) и context (dict), а возвращает bool:
True если шаг пройден, False если данные введены неправильно.
"""
import re
re_departure_city = re.compile(r'^[\w\-\s]{1,40}$')
re_arrival_city = re.compile(r'^[\w\-\s]{1,40}$')
re_date = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")
re_flight = re.compile(r"\d{4}")
re_telephone = re.compile(r"\d{11}")

from settings_dispatcher import CITY

def city_check(city):
    city_lower = city.lower()
    wrong_characters = 2
    correct_letters = 0
    variant = []
    for correct_city in CITY:
        correct_city_lower = correct_city.lower()
        letter_match=0
        if correct_city_lower[:-1] == city_lower[:-1]:
            return correct_city


        if correct_city_lower[:-1] in city_lower[:-1]:
            variant.append(correct_city)
        else:
            min_len = min(len(correct_city_lower), len(city_lower))
            if abs(len(city_lower)-len(correct_city_lower)) <= wrong_characters:
                for i in range(min_len-1):
                    if city_lower[i] in correct_city_lower[i]:
                        letter_match +=1
                    if city_lower[i] == correct_city_lower[-(i+1)]:
                        correct_letters += 1
            if abs(letter_match-len(correct_city_lower))<= wrong_characters:
                variant.append(correct_city)
            elif correct_letters > len(city_lower)//2:
                variant.append(correct_city)




    if len(variant) == 1:
        variant = variant[0]
    return variant

def handler_departure_city(text, context):
    match = re.match(re_departure_city, text)
    if match and city_check(text):
        variant = city_check(text)
        if type(variant) != list or len(variant)==1:
            context["departure_city"] = variant

            return True
        text = ''
        for v in variant:
            text += str(v)+'\n'
        context["var"] = text
    else:
        text = ''
        for v in CITY:
            text += str(v) + '\n'
        context["var"] = text
        return False


def handler_arrival_city(text, context):
    match = re.match(re_departure_city, text)
    if match and city_check(text):
        variant = city_check(text)
        if type(variant) != list or len(variant) == 1:
            context["arrival_city"] = variant

            return True
        text = ''
        for v in variant:
            text += str(v) + '\n'
        context["var"] = text
    else:
        text = ''
        for v in CITY:
            text += str(v) + '\n'
        context["var"] = text
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
from settings_dispatcher import ALL_FLY_NUMBERS
def handler_flight_selection(text, context):
    match = re.match(re_flight, text)
    if match and int(text) in ALL_FLY_NUMBERS:
        context["flight"] = text
        return True
    else:
        return False

def handler_comment(text, context):
    context["comment"] = text
    return True

def handler_right(text, context):
    if text.lower() in ['да', "нет"]:
        context["right"] = True if text =='да' else False
        print("context['right'] = ", context["right"])
        return True
    else:
        return False

def handler_telephone(text, context):
    match = re.match(re_telephone, text)
    if match:
        context["telephone"] = text
        return True
    else:
        return False

