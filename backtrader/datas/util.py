import tushare as ts 


def get_ts_pro():

    ts.set_token('1d2d0df7908eddb37a52304373ab506b4375226331fcb9e1a288af41')
    pro = ts.pro_api()
    
    return pro


def get_all_codes():
    print('code')

    pro = get_ts_pro()
    
    stock_codes = []
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(type(data))
    print(data)
    for indexs in data.index:
        stock_codes.append(data.loc[indexs].values[1])
        # print(data.loc[indexs].values[0:-1])
    

    print(len(stock_codes))


def get_all_dates():
    print('date')
    pass
