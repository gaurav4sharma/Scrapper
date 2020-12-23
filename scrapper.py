import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.in/Samsung-Internal-Solid-State-MZ-V7S500BW/dp/B07MBQPQ62/ref=sr_1_2?crid=3C144LBO4XFQZ&dchild=1&keywords=samsung%2Bevo%2B970%2Bssd%2Bm.2&qid=1605893327&sprefix=samsung%2Bevo%2B%2Caps%2C318&sr=8-2&th=1'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}

page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text().strip()
print(title)
title = soup.find(id="priceblock_ourprice").get_text().strip()
print(title.replace('₹','').replace(',','').strip())
price = float(title.replace('₹','').replace(',','').strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('Email', 'Password')
    
    subject = 'SSD Price Fell Down'
    body = 'Check the amazon Link https://www.amazon.in/Samsung-Internal-Solid-State-MZ-V7S500BW/dp/B07MBQPQ62/ref=sr_1_2?crid=3C144LBO4XFQZ&dchild=1&keywords=samsung%2Bevo%2B970%2Bssd%2Bm.2&qid=1605893327&sprefix=samsung%2Bevo%2B%2Caps%2C318&sr=8-2&th=1'
    
    msg = f'Subject: {subject}\n\n{body}'
    
    server.sendmail(
        'f20171092@pilani.bits-pilani.ac.in',
        'gaurav4sharma22@gmail.com',
        msg
    )
    
    print('Email Has been Sent')
    server.quit()