from crawler import Crawler
from util import get_all_codes, get_all_dates

class Downloader():
    def __init__(self):
        self.crawler = Crawler()

    def download_all(self, codes=None, start_date=None, end_date=None):
        codes = get_all_codes()
        dates = get_all_dates()

        


if __name__ == '__main__':
    dl = Downloader()
    dl.download_all()