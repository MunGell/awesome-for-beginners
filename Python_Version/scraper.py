import requests
from bs4 import BeautifulSoup


class PriceScraper(object):
    def __init__(self):
        pass

    def Scraper(self):
        try:
            self.ticker = "AAPL"
        except (ValueError, TypeError):
            print("Try again!")

        self.url = "https://finance.yahoo.com/quote/%s?p=%s" % (self.ticker, self.ticker)
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.arr = []

        for i in range(0, 100):
            self.current_price = self.soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find(
                'span').text
            self.arr.append(float(self.current_price))
        return self.arr
