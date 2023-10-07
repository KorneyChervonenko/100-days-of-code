""" https://www.udemy.com/course/100-days-of-code/ """
from datetime import datetime as dt
from datetime import timedelta
from pprint import pprint

import requests


def get_news(ticker_symbol: str, date: dt) -> dict:
    """ get stock data for yesterday and the day before yesterday from www.alphavantage.co """
    news_endpoint = 'https://newsapi.org/v2/everything'
    api_key = '1c5a322ed48b46e39bae5f45f649dffb'
    request_parameters = {'apiKey' : api_key,
                          'from' : str(date),
                        #   'to' : '2023-10-05',
                          'sortBy' : 'relevancy',
                        #   'sortBy' : 'popularity',
                          'qInTitle' : ticker_symbol,
                        #   'q' : ticker_symbol,
                          'language' : 'en',
                          }
    response = requests.get(url=news_endpoint, params=request_parameters)
    response.raise_for_status()
    articles = response.json().get('articles')
    return articles[:5]


def main():
    """ main function """
    yesterday = (dt.today() - timedelta(days=1)).date()
    articles = get_news('AMD', yesterday)
    for article in articles:
        print('------------------')
        print(article['title'])
        print(article['description'])
        # pprint(article)
        print('------------------')
   

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()

    sys.exit()
