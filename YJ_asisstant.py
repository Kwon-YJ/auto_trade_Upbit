import telegram
import pyupbit
import time

my_token = "888909254:AAFhueNYmy65PCZrn0EI5OQA4vFq6Fk5MfI"
bot = telegram.Bot(token = my_token)

def appetizer():
    while True:
        past_price = (((pyupbit.get_ohlcv("KRW-BTC", "week"))["open"]).tail(21)).iloc[0]
        today_price = (((pyupbit.get_ohlcv("KRW-BTC", "week"))["open"]).tail(21)).iloc[-1]
        if today_price>past_price and (past_price !=None)and(today_price !=None):
            message = "BTC-Hold"
        else:
            message = "TUSD-Hold"
        bot.send_message(chat_id = 801167350, text = message)
        time.sleep(86400)