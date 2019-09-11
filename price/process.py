import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/SMT-Genius-Popular-Willow-Cricket/dp/B07PXXTTVH/ref=sr_1_7?keywords=bat&qid=1567849803&s=gateway&sr=8-7'

head = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'+
                   '(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
def check_price():

    page = requests.get(URL, headers=head)
    soup = BeautifulSoup(page.content,'html.parser')

    title= soup.find(id='productTitle').get_text()
    title2=title.strip()

    price_str= soup.find(id='priceblock_ourprice').get_text()

    price=float(price_str[1:])

    if(price<=1000):
        send_mail(title2,price)

def send_mail(title2,price):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mailpuspaksahu@gmail.com','oskxetpxpnebgfwb')

    body='Check the amazon link\nhttps://www.amazon.in/SMT-Genius-Popular-Willow-Cricket/dp/B07PXXTTVH/ref=sr_1_7?keywords=bat&qid=1567849803&s=gateway&sr=8-7'
    msg=f'Subject: Price of {title2} fell fell down to {price}\n\n{body}'

    server.sendmail('mailpuspaksahu@gmail.com',
                    'mailpuspaksahu2@gmail.com',
                    msg)
    print("MAIL sent successfully")

while True:
    check_price()
    time.sleep(3600)

