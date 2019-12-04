# pyupbit API를 활용한 자동매매 프로그램

## 프로그램 요구사항 명세서
* 프로그램이 실행되면 업비트 원화거래소의 모든 종목의 최근 데이터를 저장한다.
* 매수기준이 충족된 종목에 한해서 가상의 매수 주문을 넣고 money 파일의 숫자(가상의 돈)을 감소시킨다.
* 정해진 시간에 대해 매수된 종목을 일괄 매도하고 money 파일의 숫자(가상의 돈)을 증가시킨다.


* 매수 기준 : 현재가 > 금일 시가 + ATR(14) * 0.5
* 매도 기준 : 6시, 12시, 18시, 24시 일괄 매도

## 설치모듈
* pyupbit (pip install pyupbit)

## 프로그램 사용방법
* money 파일에 원하는 금액을 입력한다 (오천만원 입력 예 : 50000000.0)
* main.py를 실행한다.
*
* 주의사항 : 실거래를 위해서는 본인이 직접 API KEY를 발급받아 key.pickle를 수정해야한다.

