import pyupbit
from Order import order
from ATR import day_ago, get_TR, get_ATR
import time
import datetime
from Data_Group import upbit, List_tickers, Q1, Q2, Q3, Q4, Q5
import pickle
import os


while(True):
    for i in range(0,87):
        order(List_ohlcv[i], List_tickers[i])#핵심, 코어







#appetizer // 시그널만 보내는 레이더 역할
#main // BTC_goto_TUSD 와 TUSD_goto_BTC를 분기하기 위한 메인
#Exchnage_Point // today - 18160(예시) 을 range로 정의하고 range내의 high 값에서 2.7ATR을 뺀 값을 호출
#BTC_goto_TUSD // BTC의 현재가 < Exchnage_Point 이면 goto_TUSD
#TUSD_goto_BTC // TUSD의 현재가 < Exchnage_Point 이면 goto_TUSD
#위 두 함수는 역 관계에 놓일 뿐 동일한 기능울 수행한다.

#청산과 동시에 텔레그램 메세지 전송



#while(data!=None):
    #data = pybithumb.get_ohlcv