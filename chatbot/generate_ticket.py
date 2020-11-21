import os
from io import BytesIO
from random import randint

import requests
from PIL import Image, ImageDraw, ImageFont
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

PATH_BASE_PHOTO = "Base.PNG"
PATH_FONT = "fnd.ttf"
pam = str(randint(1, 7))
PATH_AVATAR = f"Avatars\\var{pam}.png"


def generate_ticket(name, email):
    # get an image
    base = Image.open(PATH_BASE_PHOTO).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    X_size, Y_size = txt.size
    fnt = ImageFont.truetype(PATH_FONT, 22)

    d = ImageDraw.Draw(txt)
    d.text((X_size - 300, Y_size // 2 - 75), name, font=fnt, fill=(255, 255, 255), )
    d.text((X_size - 350, Y_size // 2 - 25), email, font=fnt, fill=(255, 255, 255, 255))
    base = Image.alpha_composite(base, txt)

    avatar_base = Image.open(PATH_AVATAR).convert("RGBA").resize((125, 125))

    base.paste(avatar_base, (0, Y_size - 125))

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file


try:
    f = open('Files\\probe.png')
    f.close()
except FileNotFoundError:
    pam = str(6)
    PATH_AVATAR = f"Avatars\\var{pam}.png"
    generate_ticket("111", "aaa")
