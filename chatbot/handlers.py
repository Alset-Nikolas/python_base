
"""
Handler - функция, которая принимает на вход text (такст входящего сообщения) и context (dict), а возвращает bool:
True если шаг пройден, False если данные введены неправильно.
"""
import re
re_name = re.compile(r'^[\w\-\s]{3,40}$')
re_email = re.compile(r"(\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b)")
def handler_name(text, context):
    match = re.match(re_name, text)
    if match:
        context["name"] = text
        return True
    else:
        return False


def handler_email(text, context):
    matches = re.findall(re_email, text)
    print(len(matches)>0)
    if len(matches)>0:
        context["email"] = text
        return True
    else:
        return False