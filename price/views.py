from django.shortcuts import render,redirect
from .forms import new_entry
from .models import entry

import requests
from bs4 import BeautifulSoup
import smtplib
import time

x=0
def details(request):
    if(request.method=='POST'):
        x=new_entry(request.POST)
        if x.is_valid():
            new_item=entry(url=request.POST['url'],email=request.POST['email'],price=request.POST['price'])
            new_item.save()
            wholeprocess(request.POST)
            return redirect('notice1')

    else:
        x=new_entry()
    context={'x':x}
    return render(request,'price/index.html',context)
def notice1(request):
    return render(request,'price/notice1.html')


def wholeprocess(a):
    URL = a['url']
    email=a['email']
    req_price=float(a['price'])

    head = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'+
                       '(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    def check_price():
        page = requests.get(URL,headers=head)
        soup = BeautifulSoup(page.content,'html.parser')
        title= soup.find(id='productTitle').get_text()
        title2=title.strip()
        price_str= soup.find(id='priceblock_ourprice').get_text()
        list=[l for l in price_str[2:-3] if l not in [',']]
        price2=''.join(list)

        price=float(price2)
            

        if(price<=req_price):
            global x
            x=1
            send_mail(title2,price)
    def send_mail(title2,price):
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('mailpuspaksahu@gmail.com','oskxetpxpnebgfwb')
        body='Check this amazon link\n'+URL
        msg=f'Subject: Price of {title2} fell fell down to {price}\n\n{body}'
        server.sendmail('mailpuspaksahu@gmail.com',email,msg) 
    
    while x==0:
        check_price()
        time.sleep(3600)
       


