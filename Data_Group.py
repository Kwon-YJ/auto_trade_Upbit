import pickle
import time
import datetime
import pyupbit

with open("Key_Value.pickle","rb") as fr:
    Key_Value = pickle.load(fr)
upbit = pyupbit.Upbit(Key_Value[0], Key_Value[1])

List_alltickers = pyupbit.get_tickers()
List_tickers = [s for s in List_alltickers if 'KRW' in s]

now = datetime.datetime.now()
Q1 = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(hours = 9)
Q2 = Q1 + datetime.timedelta(hours = 6)
Q3 = Q2 + datetime.timedelta(hours = 6)
Q4 = Q3 + datetime.timedelta(hours = 6)
Q5 = Q4 + datetime.timedelta(hours = 6)


