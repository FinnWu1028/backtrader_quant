import tushare as ts 
from util import get_ts_pro
import pymongo
from datetime import datetime
import time


class Crawler:
    def __init__(self):
        self.pro = get_ts_pro()
        

    def crawl_stocks(self, codes, start_date=None, end_date=None):
        if codes is None:
            print('[crawl_stocks] codes is None')
            return 

        if start_date is None or end_date is None:
            print('[crawl_stocks] data is None')
            return
        
        
        for code in codes:
            print('cddc  %s '%  code)
            self.crawl(code, start_date, end_date)
            
                    



    def crawl(self, ts_code, ktype='day', start_date=None, end_date=None):
        for _ in range(3):
            df = []
            try:
                if code:
                    
                    df = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_date, end_date=end_date)
                    print('code %s len %d ' % (code, len(df.raws)))
                    print(code)

                else:
                    print('code is none')
            except:
                time.sleep(1)

            else:
                print('end')
                return df


if __name__ == '__main__':
    dc = Crawler()
    start   =  '20110101'
    end     =  '20110130'

    code = '000001.SZ'
    codes = ['000001.SZ', '000009.SZ']
    
    
    df = []
    df = dc.crawl(ts_code=code, start_date=start, end_date=end)
    dc.crawl_stocks(codes, start_date=start, end_date=end)

    print(df)