from __future__ import (absolute_import, division, print_function, unicode_literals)

from datetime import datetime
import os.path
import sys
import backtrader as bt 
import tushare as ts 
import pandas as pd
import numpy as np

class SmaCross(bt.Strategy):

    params = dict(
        pfast = 5,
        pslow = 10
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)
        sma2 = bt.ind.SMA(period=self.p.pslow)
        self.crossover = bt.ind.CrossOver(sma1, sma2)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
            elif self.crossover < 0:
                self.sell()

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

code = '000001.SZ'
start   =  '20180101'
end     =  '20200229'


df = ts.pro_bar(ts_code=code, adj='qfq', start_date=start, end_date=end)
# df['openinterest'] = 0
print(df.columns)


df = df.sort_index(axis=0, ascending=False)
df.index = pd.to_datetime(df.trade_date).dt.date

#df = df[['open','high','low','close','vol', 'openinterest']]
df = df[['open','high','low','close','vol']]

print('df size %d %d '% (df.shape[1], df.shape[0]))
for index, row in df.iterrows():
    print(index, row['open'], row['high'], row['low'], row['close'], row['vol'])


data = bt.feeds.PandasData(dataname=df, 
                            fromdate=datetime(2018, 1, 1),                               
                            todate=datetime(2020, 2, 29) )

cerebro.adddata(data) 

cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.001)
cerebro.addsizer(bt.sizers.FixedSize, stake = 5000)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# plot 有问题，说参数空的太多

# cerebro.plot()