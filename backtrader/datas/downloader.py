from crawler import Crawler
from util import get_all_codes, get_all_dates

class Downloader():
    def __init__(self):
        self.crawler = Crawler()

    def download_all(self, start_date=None, end_date=None):
        
        codes = get_all_codes()
        dates = get_all_dates(start_date, end_date)

        self.crawler.crawl_stocks(codes, start_date, end_date)

        


if __name__ == '__main__':
    dl = Downloader()
    start = '20190101'
    end = '20190201'

    dl.download_all(start_date=start, end_date=end)