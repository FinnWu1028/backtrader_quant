import tushare as ts 
import math


def get_ts_pro():

    ts.set_token('1d2d0df7908eddb37a52304373ab506b4375226331fcb9e1a288af41')
    pro = ts.pro_api()
    
    return pro


def get_all_codes():
    print('code')

    pro = get_ts_pro()
    
    stock_codes = []
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # print(type(data))
    # print(data)
    for indexs in data.index:
        stock_codes.append(data.loc[indexs].values[0])
        # print(data.loc[indexs].values[0])
    
    print('stocks has %d codes' % len(stock_codes))


    stock_sp_col = [x for x in range(len(stock_codes))]
    print(stock_sp_col)
    
    for i in stock_sp_col:
        stock_sp_col[i] = math.ceil(i / 100)
    
    stock_sp_col[0] = 1
    stock_dict = dict(zip(stock_codes, stock_sp_col))
    
    return stock_dict


def save_stock_dict_to_db():
    pass


def get_all_dates(start=None, end=None):

    dates = []
    df = []
    pro = get_ts_pro()

    if start is None or end is None:
        print('start or end is None')
        return None
    
    
    df = pro.trade_cal(exchange='', start_date=start, end_date=end)
    
    for indexs in df.index:
        
        if df.loc[indexs].values[2] == 1:
            dates.append(df.loc[indexs].values[1])
        
    
    print('dates has %d days from %s to %s ' % (len(dates), start, end))

if __name__ == '__main__':
    get_all_codes()
    start   = '20190101'
    end     = '20190201'
    get_all_dates(start=start, end=end)


