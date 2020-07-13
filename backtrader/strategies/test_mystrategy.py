import backtrader as bt 
import backtrader.indicators as btind
import backtrader.feeds as btfeeds




class test_DataFeeds(bt.Strategy):
    def __init(self):
        sma1 = btind.SimpleMovingAverage(self.datas[0], peroid=self.p.peroid)

        sma2 = btind.SimpleMovingAverage(sma1, period=self.p.period)

        something = sma2 - sma1 + self.data.close

        sma3 = btind.SimpelMovingAverage(sma3, period=self.p.period)

        greater = sma3 > sma

        sma3 = btind.SimpleMovingAverage(greater, period=self.p.period4)





class test_Params(bt.Strategy):
    # dict
    params1 = dict(period=20)

    # tuple
    params2 = (('period', 20),) 

### line ###
    def __init__(self):
        self.movav = btind.SimpleMovingAverage(self.data, period=self.p.period)

    def next(self):
        if self.movav.lines.sma(0) > self.data.close[0]:
            print('simple moving average is greater than the closing price')

    ## xx.lines   xx.l
    #  xx.lines.name  xx.lines_name
    # 
    #  class SimpleMovingAverage(Indicator):
    #      lines = ('sma') 
    #  
    # self.lines[0]      self.lines.sma  
    # 
    #     
  
### slice ###

### operation ###


class test_Params(bt.Strategy):
    params1 = dict(period=20)
    def __init__(self):
        sma0 = btind.SMA(self.data0, period=5)
        sma1 = btind.SMA(self.data1, period=15)

        self.buysig = sma0 > sma1()

    def next(self):
        if self.buysig[0]:
            print('daily sma is greater than weekly sma1')

### Operators, using natural constructs ###
### stage 1###
class test_Strategy_operation(bt.Strategy):
    def __init__(self):
        sma = btind.SMA(self.data0, period=5)

        close_over_sma = self.data.close > sma
        sma_dist_to_high = self.data.high - sma
        sma_dist_small = sma_dist_to_high < 3.5 

        sell_sig = bt.And(close_over_sma, sma_dist_small)
