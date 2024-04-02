import time
import ccxt
import telebot

# Replace with your actual bot token and chat ID
bot_token = "7011162475:AAHuSXG-0g0xCLAJQdxAtgu-L5uyiVcyHPo"
chat_id = "1149619686"

# DEFINE YOUR EXCHANGE AND TICKERS:
my_exchange = 'Binance' # example of crypto exchange 
ticker1 = 'PYTH' # first ticker of the crypto pair
ticker2 = 'USDT' # second ticker of the crypto pair
method_to_call = getattr(ccxt,my_exchange.lower()) # retrieving the # method from ccxt whose name matches the given exchange name
# Create a Telegram Bot object  
bot = telebot.TeleBot(bot_token)
iterations=1
last_closing_prince=0
closing_price=0


while 1:
    exchange_obj = method_to_call() # defining an exchange object
    pair_price_data = exchange_obj.fetch_ticker(ticker1+'/'+ticker2)
    last_closing_prince=closing_price
    closing_price = pair_price_data['close']
    print ("PYTH: %1.4f  Iterations: %4d " % (closing_price, iterations))
    iterations=iterations +1


    if closing_price>0.99 and closing_price>last_closing_prince:

        # Send message with PYTH price
        message = f"Current PYTH price: ${closing_price:.4f} USD"
        bot.send_message(chat_id, message)


