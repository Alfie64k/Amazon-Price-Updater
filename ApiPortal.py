import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ='https://www.amazon.co.uk/Apple-MGJ83B-A-iPhone-64GB/dp/B08L5Q2M7J/ref=sr_1_4?dchild=1&keywords=Iphone+12&qid=1603727373&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

UserEmail = input("Please enter your email? ")

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:-3])

    print(converted_price)
    print(title.strip())
    
    if(converted_price < 799.00):
        send_mail()
        
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('cameronadam48@gmail.com', 'jncazpqhuluoybwo')
    
    subject = 'Price fell down!'
    body = 'Check the Amazon link! https://www.amazon.co.uk/Apple-MGJ83B-A-iPhone-64GB/dp/B08L5Q2M7J/ref=sr_1_4?dchild=1&keywords=Iphone+12&qid=1603727373&sr=8-4'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'cameronadam48@gmail.com',
        (UserEmail),
        (msg)
    )
    print("Email has been sent")
    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)

