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


def generate_ticket(departure_city, arrival_city, date, flight, comment, telephone):
    # get an image
    base = Image.open(PATH_BASE_PHOTO).convert("RGBA")
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    X_size, Y_size = txt.size
    fnt = ImageFont.truetype(PATH_FONT, 12)


    idraw = ImageDraw.Draw(txt)
    x0=60; y0=80
    dy=12
    idraw.text((x0, y0), departure_city, font=fnt, fill=(0, 0, 0), )
    idraw.text((3*x0-10, y0), arrival_city, font=fnt, fill=(0, 0, 0))
    idraw.text((x0, y0+2*dy), date, font=fnt, fill=(0, 0, 0), )
    idraw.text((3*x0-10, y0+2*dy), flight, font=fnt, fill=(0, 0, 0))
    idraw.text((x0, y0+4*dy-5), comment, font=fnt, fill=(0, 0, 0), )
    idraw.text((x0, y0+5*dy+3), telephone, font=fnt, fill=(0, 0, 0))
    base = Image.alpha_composite(base, txt)

    base.show()
    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file


if __name__ == "__main__":
    generate_ticket(departure_city="Москва",
                    arrival_city="Питер",
                    date="12-11-2021",
                    flight="2313",
                    comment="УУУУУ",
                    telephone="89999999999")
