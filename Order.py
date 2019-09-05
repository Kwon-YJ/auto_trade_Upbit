import pyupbit
import time
import datetime
from ATR import day_ago, get_TR, get_ATR
from Data_Group import upbit, Q1, Q2, Q3, Q4, now
import pickle

def order(ticker_data, ticker_name):
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    if ticker_name not in data:
        buy_order(ticker_data, ticker_name)
    else:
        sell_order(ticker_data, ticker_name)
                
def buy_order(ticker, ticker_name):
    a = pyupbit.get_current_price(ticker_name) # 현재가
    b = 0.5 * get_ATR(ticker) + day_ago(2, 'close', ticker).values # 전일종가 + 0.5ATR
    if a>b:
        f = open('money', 'r')
        krw = float(f.readline())
        f.close
        orderbook = pyupbit.get_orderbook(ticker_name) #해당 코인 호가 조회
        sell_price = orderbook[0]['orderbook_units'][0]['ask_price'] #최우선 매도 호가 계산
        unit = krw*0.1/sell_price #매수 수량
        print("매수:" + ticker_name + ", 단가 :", sell_price, '수량:', unit)
        f = open('money', 'w')
        money = str(float(krw) - (sell_price * unit))
        f.write(money)
        f.close
        print(datetime.datetime.now())
        with open('data.pickle', 'rb') as f:
                data = pickle.load(f)              
        data[ticker_name] = unit
        with open('data.pickle', 'wb') as f:
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def sell_order(ticker_data, ticker_name):
    if Q1 < datetime.datetime.now() < Q1 + datetime.timedelta(seconds=30)or Q2 < datetime.datetime.now() < Q2 + datetime.timedelta(seconds=30)or Q3 < datetime.datetime.now() < Q3 + datetime.timedelta(seconds=30)or Q4 < datetime.datetime.now() < Q4 + datetime.timedelta(seconds=30):
        f = open('money', 'r')
        krw = float(f.readline())
        f.close
        price = pyupbit.get_current_price(ticker_name)
        with open('data.pickle', 'rb') as f:
                data = pickle.load(f)
        unit = data[ticker_name]
        f = open('money', 'w')
        money = str(float(krw) + (price * unit))
        f.write(money)
        f.close
        print("매도:" + ticker_name + ", 단가 :", price, '수량:', unit)
        print(datetime.datetime.now())
'''
def balance_CoinToKrw(ticker_name):
        a = upbit.get_balance(ticker_name)[0]
        b = pyupbit.get_current_price(ticker_name)
        return format((a*b), 'f')
#위 함수는 실제투자시에만 요구된다. 
'''