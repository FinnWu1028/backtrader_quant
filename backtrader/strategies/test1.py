from __future__ import (absolute_import, division, print_function,
unicode_literals)
import backtrader as bt
import tushare as ts
import pandas as pd
from datetime import datetime


class StrtegySB(bt.Strategy):

    params = (
        ('exitbars', 5),
        ('maperiod', 15),
    )


    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.sma = bt.indicators.SimpleMovingAverage(self.datas[0], period=self.params.maperiod)


    def notify_order(self, order):

    #   - Submitted: sent to the broker and awaiting confirmation
    #   - Accepted: accepted by the broker
    #   - Partial: partially executed
    #   - Completed: fully exexcuted
    #   - Canceled/Cancelled: canceled by the user
    #   - Expired: expired
    #   - Margin: not enough cash to execute the order.
    #   - Rejected: Rejected by the broker

        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:           
            print('order isbusy %s ' % order.isbuy())
            if order.isbuy():
                self.log('BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm

            elif order.issell():
                self.log('SELL EXECUTED, Price %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))


            self.bar_executed = len(self)
            # print(self.bar_executed)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        else:
            self.log('order unknow')
        
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                 (trade.pnl, trade.pnlcomm))


    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])

        if self.order:
            return

        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy() 

            # if self.dataclose[0] < self.dataclose[-1]:
            #     if self.dataclose[-1] < self.dataclose[-2]:
            #         self.log('BUY CREATE, %.2f' % self.dataclose[0])
            #         self.order = self.buy()

        else:
            
            if self.dataclose[0] < self.sma[0]:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])   
                self.order = self.sell() 

            # if len(self) >= (self.bar_executed + self.params.exitbars):
            #     self.log('SELL CREATE, %.2f' % self.dataclose[0])   
            #     self.order = self.sell()


cerebro = bt.Cerebro()
cerebro.addstrategy(StrtegySB)

code = '000001.SZ'
start   =  '20190601'
end     =  '20200630'

df = ts.pro_bar(ts_code=code, adj='qfq', start_date=start, end_date=end)

df = df.sort_index(axis=0, ascending=False)

#print(df)


df.index = pd.to_datetime(df.trade_date)
print(df.index)
print(df)

print(df.columns)
df = df[['open','high','low','close','vol']]
data = bt.feeds.PandasData(dataname=df, 
                            fromdate=datetime(2019, 6, 1),                               
                            todate=datetime(2020, 6, 30) )

cerebro.adddata(data, name=code)
cerebro.adddata(data, name='1212')


cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.001)
cerebro.addsizer(bt.sizers.FixedSize, stake = 100)

print(cerebro.datas[0])

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
