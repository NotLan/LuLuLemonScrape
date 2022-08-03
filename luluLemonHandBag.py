from time import sleep

import requests
from bs4 import BeautifulSoup
import gmail

response = requests.get("https://shop.lululemon.com/p/bags/Everywhere-Belt-Bag/_/prod8900747?color=47748&sz=ONESIZE")
response1 = requests.get("https://shop.lululemon.com/p/bags/Everywhere-Belt-Bag/_/prod8900747?color=23315&sz=ONESIZE")
response2 = requests.get("https://shop.lululemon.com/p/bags/Everywhere-Belt-Bag/_/prod8900747?color=33928&sz=ONESIZE")
response3 = requests.get('https://shop.lululemon.com/p/bags/Everywhere-Belt-Bag/_/prod8900747?color=*&sz=ONESIZE')


items = [
    response,
    response1,
    response2,
    response3
]

for x in items:

    soup = BeautifulSoup(response1.content, "html.parser")
    element = soup.find_all("button", class_="button-qfnRT lll-text-button purchase-methods_addToBag__1O17H buttonPrimary-1m-xO buttonBlock-3QinT")[0].attrs['data-lulu-track']

    while "disabled" in element:
        print("Out of stock waiting and checking next item in 1 minute...")
        sleep(60)
    else:
        gmail.send_mail()
