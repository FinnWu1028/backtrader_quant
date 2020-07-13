from __future__ import (absolute_import, division, print_function, unicode_literals)

from backtrader as bt 
import datetime as datatime 
import sys


class SellStopLoss(bt.Strategy):
    prams = dict(
        p_downdays=3,
        p_stoploss=0.05,
        p_takeprofit = 0.1,
        limit=0.005,
        limday=3,
        limdays=1000,
        hold=10,
        usebracket=False,
        switchplp2=False
    )

    def notify_order(self, order):
        print('{}: Order ref : {} / Type {} / Status {} '.format(
            self.data.datetime.date(0),
            order.reg, 'Buy' * order.isbuy() or 'sell',
            order.getstatusname()
        ))

        if order.status == order.Completed:
            self.holdstart = len(self.ref)

    def __init__(self):
        self.dataclose = self.datas[0].close
        sma = bt.ind.SMA(peroid=self.p.p_downdays + 1, plot = True)
        self.orefs = list()

    def next(self):
        if self.orefs:
            return

        if not self.position:
            lastcloses = list()
            for i in range(self.p.p_downdays + 1):
                lastcloses.append(self.dataclose[-i])

        if lastcloses == sorted(lastcloses):
            close = self.dataclose[0]
            p1 =  close * (1.0 -self.p.limit)
            p2 = p1 - self.p.p_stoploss * close
            p3 = p1 + self.p.p_takeprofit *close

            valid1 = timedelta(self.p.limday)
            valid2 = valid3 = timedelta(self.p.limdays)

            os = self.buy_bracket(
                price=p1, valid=valid1,
                stopprice=p2, stopargs=dict(valid=valid2),
                limitprice=p3, limitargs=dict(valid=valid3),

            )
        
            self.orefs = [o.ref for o in os]
            








