def day_ago(day,ohlcv,ticker):
    a = ticker.tail(day)
    b = a[ohlcv]
    c = b.head(1)
    return c

def get_TR(date,ticker):
    a = day_ago(date,'high',ticker)
    b = day_ago(date,'low',ticker)
    c = a.values-b.values

    aa = day_ago(date,'high',ticker)
    bb = day_ago(date+1,'close',ticker)
    cc = abs(aa.values-bb.values)

    aaa = day_ago(date,'low',ticker)
    bbb = day_ago(date+1,'close',ticker)
    ccc = abs(aaa.values-bbb.values)

    return max(c,cc,ccc)

def get_ATR(ticker):
    value = 0
    for i in range(15):
        TR = get_TR(i+2,ticker)
        value = value + TR
    return value/15

