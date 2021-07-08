from keys import *
import smtplib
import time
from binance.client import Client
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime 

def send(coinname, price, recieversEmail):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sendersEmail, senderspassword)

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


    plt.style.use('seaborn')
    x_vals = []
    y_vals = []

    def animate(i):
        # Fetch Coin details from the API
        price = client.get_symbol_ticker(symbol=coinname)
        
        # If price Target hit, send email and close graph
        if alert >= float(price['price']):
            send(coinname, price, recieversEmail)
            print("ALERT Email sent!!")
            plt.close()
            return

        x_vals.append(datetime.now())
        y_vals.append(price['price'])

        plt.cla()

        plt.gcf().canvas.set_window_title(coinname + ' Live Price')
        
        plt.xlabel('Date')
        plt.ylabel('Price($)')
        plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
        plt.tight_layout()
        
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.show()

    print(price)
    time.sleep(3)

        












