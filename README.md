# Cryptocurrency Price Alert
Sends an Alert Email as soon as your Cryptocurrency hits a trigger price.

## Why was it needed?
Due to the highly volatile nature of Cryptocurrencies this script comes in handy when you're day trading. <br>
India's Top cypto exchange <b>"WazirX"</b> lacks this feature where you can set a <b>Trigger Price</b> for your favourite cryptocurrency.<br>
This script helps in timing the market and taking decisions accordingly.

## Prerequisites
1. An account on <a href="https://www.binance.com">Binance.com</a>.
2. Binance API Key and API Secret Key.
3. Follow <a href="https://www.youtube.com/watch?v=qg-oboAY8rM">this</a> video for help regarding the above mentioned point.
4. A working dummy email ID.

## How to use?
1. The best way to use my script is to firstly clone the git repo where you want to.
2. Go to <b>keys.py</b> and enter your Binance API key and Secret Key next to the corresponding variables.
3. Enter your dummy email account details in keys.py.
4. Go to <b>main.py</b> and run it.
5. Enter the Crypto of your choice and set the Trigger Price.

Optional: If you want a live price chart to be displayed as well, please run "withliveplot.py" instead of "main.py" in step (4)

## What happens behind the scene?
1. This script fetches the price of the crypto via the Binance API every 3 seconds.
2. As soon as the current price becomes less than or equal to the Alert price, this script sends an email alert to the user's main email.

