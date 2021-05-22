from keys import *
import smtplib
import time
from binance.client import Client

def send(coinname, price, recieversEmail):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sendersEmail, sendersPassword)

    message = "Your Alert for {} has been triggered. \n Current Price of {} = {}".format(coinname, coinname, price['price'])

    server.sendmail(sendersEmail, recieversEmail, message)

    server.quit()

if __name__ == "__main__":
    
    client = Client(api_key, api_secret)
    
    #Enter the email address that you want to get your alert in.
    recieversEmail = "theboycote@gmail.com" 

    #alert
    coinname = input("Enter the coin symbol: ")
    coinname = (coinname + 'USDT').upper()
    alert = float(input("Enter the alert amount: "))
    # get latest price from Binance API
    price = client.get_symbol_ticker(symbol=coinname)
    print(price, "outside")
    while alert < float(price['price']):
        price = client.get_symbol_ticker(symbol=coinname)
        # print full output (dictionary)
        print(price)
        time.sleep(3)
    else:
        send(coinname, price, recieversEmail)
        print("ALERT Email sent!!")

