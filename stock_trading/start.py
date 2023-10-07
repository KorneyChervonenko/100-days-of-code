""" https://www.udemy.com/course/100-days-of-code/ """
from stockdata import get_2days_stockdata
from newsdata import get_news
delta_threshold = 1
COMPANY = 'AMD'

def main():
    """ main function """
    data = get_2days_stockdata(COMPANY)
    day_before_yesterday_price, yesterday_price = data.values()
    delta_price = yesterday_price - day_before_yesterday_price
    delta_symbol = '▲' if delta_price > 0 else '▼'
    yesterday = max(data.keys())
    if abs(delta_price) > delta_threshold:
        delta_percentage = round((abs(delta_price) / yesterday_price) * 100, 2)
        print(f'stock price {delta_symbol} {delta_percentage}% {list(data.values())}')
        articles = get_news(COMPANY, yesterday)
        for article in articles:
            print('------------------')
            print(article['title'])
            print(article['description'])
            print('------------------')

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()

    sys.exit()
