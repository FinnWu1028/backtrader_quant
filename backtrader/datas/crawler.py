import tushare as ts 
from util import get_ts_pro
import pymongo
from datetime import datetime
import time
from pymongo import UpdateOne
from database import MY_DB

class Crawler:
    def __init__(self):
        self.pro = get_ts_pro()
        

    def crawl_stocks(self, codes, start_date=None, end_date=None):
        print(codes)
        if codes is None:
            print('[crawl_stocks] codes is None')
            return 

        if start_date is None or end_date is None:
            print('[crawl_stocks] data is None')
            return
        
        
        for code in codes:
            self.crawl(code, start_date=start_date, end_date=end_date)
            
                    

    def crawl(self, code, ktype='day', start_date=None, end_date=None):
        for _ in range(3):
            df_daily = []
            
            if code: 
                df_daily = ts.pro_bar(ts_code=code, adj='qfq', start_date=start_date, end_date=end_date)
                # print(df)
                if df_daily is not None:
                    print('%s has %d records from %s to %s'% ( code, len(df), start_date, end_date))
                    break
                
        print(df_daily) 

        for df_index in df_daily.index:
            print(type(df_daily.loc[df_index]))
            doc = dict(df_daily.loc[df_index])
            print(doc)
        #     doc['code'] = code

        update_requests = []
        update_requests.append(
            UpdateOne(
                {'ts_code' : doc['ts_code'], 'date': doc['date']},
                {'$set': doc},
                upsert=True
            )
        )

        if len(update_requests) > 0:


            collection_name =  
            update_result = MY_DB[collection_name].bulk_write(update_requests, ordered=False)
            print('Save index %s, code: %s, inserted: %4d, modified: %4d'
                    % (collection_name, code, update_result.upserted_count, update_result.modified_count), flush=True)



if __name__ == '__main__':
    dc = Crawler()
    start   =  '20110101'
    end     =  '20110130'

    code = '000001.SZ'
    codes = ['000001.SZ', '000009.SZ']
    
    
    df = []
    pro = get_ts_pro()

    # df = ts.pro_bar(ts_code=code, start_date=start, end_date=end)
    # print(df)
    dc.crawl_stocks(codes, start_date=start, end_date=end)

