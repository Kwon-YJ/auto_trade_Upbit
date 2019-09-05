import pyupbit
from Order import order
from ATR import day_ago, get_TR, get_ATR
import time
import datetime
from Data_Group import upbit, List_tickers
from Data_Group import Q1, Q2, Q3, Q4
import pickle

while(True):
    data = {}
    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    List_ohlcv = []
    for i in range(87): #총 87개의 코인이 업비트 원화거래소에서 사용된다.
        List_ohlcv.append(pyupbit.get_ohlcv(List_tickers[i]))
        time.sleep(0.09) #논오버클럭 라이젠 2600 CPU기준으로 0.09초의 슬립이 없을 경우, 리퀘스트속도가 CPU속도를 따라잡지 못해 NoneType에러가 발생했다.
    while(True):
        for i in range(0,87):
            order(List_ohlcv[i], List_tickers[i])
        if Q4 + datetime.timedelta(hours = 1/60) < datetime.datetime.now() < Q4 + datetime.timedelta(hours = 1/50): #날짜가 바뀌면 Q값도 조정
            Q1 += datetime.timedelta(hours = 24)
            Q2 += datetime.timedelta(hours = 24)
            Q3 += datetime.timedelta(hours = 24)
            Q4 += datetime.timedelta(hours = 24)
            break
    