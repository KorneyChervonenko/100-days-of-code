""" https://www.udemy.com/course/100-days-of-code/ """
from datetime import datetime as dt
from pprint import pprint

import requests


def get_2days_stockdata(ticker_symbol: str) -> dict:
    """ get stock data for yesterday and the day before yesterday from www.alphavantage.co """
    alphavantage_endpoint = 'https://www.alphavantage.co/query'
    api_key = 'P7FEEGDXXECOBSTM'
    request_parameters = {'apikey' : api_key,
                          'function' : 'TIME_SERIES_DAILY',
                          'symbol' : ticker_symbol,
                          }
    response = requests.get(url=alphavantage_endpoint, params=request_parameters)
    response.raise_for_status()
    data = response.json().get('Time Series (Daily)')
    data = {dt.strptime(date, '%Y-%m-%d').date():info for date, info in data.items()}
    dates = sorted(data.keys())
    last2date_data = {date : float(data[date].get('4. close')) for date in dates[-2:]}
    return last2date_data


def main():
    """ main function """
    data = get_2days_stockdata('AMD')
    pprint(data)
    

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
