""" https://www.udemy.com/course/100-days-of-code/ """
# to compile a list of all the places for rent in San Francisco 
# from $2,800 up to $3,000 per month and it has to have at least one bedroom
import json
import re
import time
import urllib.parse
from urllib.parse import parse_qs, urlparse
from collections import namedtuple
from pprint import pprint

import bs4
import requests
import xlsxwriter

base_url = 'https://www.zillow.com/san-francisco-ca/rentals/'
EXCELFILE = 'zillow.xlsx'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'Accept-Encoding': 'gzip, deflate, br',
          'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,uk;q=0.6',
          'Cookie': 'x-amz-continuous-deployment-state=AYABeDucO0QKUciaqDTua+Ne5LsAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADEt0b0ib7yUdOZgGfAAwcWgtvx6F2nU5%2FTAEzvfyOW2tFCDvLRbNrS0pFU2S53WDDl0yDkKIuelEKba4INckAgAAAAAMAAQAAAAAAAAAAAAAAAAAAPIxmp3Uyz8vczXYsWSBnJ%2F%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxAXdHREYlst4AML2+WNzSlSjzFuuUsD0lbrh65zFuuUsD0lbrh6w==; zguid=24|%24168f965f-64a4-4018-8db7-e249c111d085; zgsession=1|77737b1c-eea1-4dd7-9115-9737202c33aa; _ga=GA1.2.586780656.1697976481; _gcl_au=1.1.1105346262.1697976481; DoubleClickSession=true; zjs_anonymous_id=%22168f965f-64a4-4018-8db7-e249c111d085%22; zjs_user_id=null; zg_anonymous_id=%223506cf0c-6fe6-4769-ad3a-a94af42650a5%22; __pdst=3deb531a49d643bea2715e96623a3944; pxcts=a5288e3c-70d3-11ee-bd2b-9c81279e85c7; _pxvid=a5287f21-70d3-11ee-bd2b-7d2a42ec5cbf; _hp2_id.1215457233=%7B%22userId%22%3A%225387914054266090%22%2C%22pageviewId%22%3A%226791500064381303%22%2C%22sessionId%22%3A%227470607733872365%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; AWSALB=lUHLsQ8vVDJCmWeQgDw+yn0M3GKcJo4MVHe5Hi8nMPG6XZ312AagHEhFrg2S4a5+LyT6qFSdQDpC04n/LAlQwPYfvFNKQcfwZy1wVWH0s4Kv1lzm2PxkVHODu9QA; AWSALBCORS=lUHLsQ8vVDJCmWeQgDw+yn0M3GKcJo4MVHe5Hi8nMPG6XZ312AagHEhFrg2S4a5+LyT6qFSdQDpC04n/LAlQwPYfvFNKQcfwZy1wVWH0s4Kv1lzm2PxkVHODu9QA; JSESSIONID=6766B1322AD453271DD1B9E494C455B1; search=6|1700811178256%7Crect%3D37.9147417949056%252C-122.3383167203514%252C37.69230459360572%252C-122.74000434242171%26rid%3D20330%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26listPriceActive%3D1%26beds%3D1-%26price%3D0-525671%26mp%3D0-3000%26fs%3D0%26fr%3D1%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0920330%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; _pin_unauth=dWlkPVpHVXlNVGxqWW1NdE1qSTJOeTAwTmpOaExUazJOakV0TWpnME5UazRZVGd6TkROaQ; _fbp=fb.1.1697976490071.593044510; _clck=16ozl1e|2|fg5|0|1390; __gads=ID=e4e9db78625244ad:T=1697976498:RT=1698219070:S=ALNI_Mb9lYiGC4qjT4p7QsQIo-9wWGzDxA; __gpi=UID=00000c9ffad8ceaa:T=1697976498:RT=1698219070:S=ALNI_MZkZjA3bKzgYo7gEiqkH5OqqidOuA; FSsampler=410191420; _csrf=oK3elc3Jj43xGrXEgKWBkbvW; _pxhd=18jLMwWNJW%2FIJ8bTGMNKfaFSal55HIu5bdJoyJlq7NKLg1lutoMU8lh5%2Fk4NzMTvA1KnSNWYAdX%2FpX1eMzwkCQ%3D%3D%3A6i5s9vtTBw53rltDSrLCUQ-jyXVeUNeyWQFzE4AZ%2FXZrShkCxJf6502sIyK-cUFHU3xyJsLeDhZBoNjKtiFMcsIKOQlV6peksRH9XM-NALY%3D; zgcus_aeut=AEUUT_541eee14-71b0-11ee-b41f-962af788e385; zgcus_aeuut=AEUUT_541eee14-71b0-11ee-b41f-962af788e385; rjs-trace=d5548f44ff2a7bbd8f6a172ee6:1790c2d2fc63da00f51d05180adae556:; optimizelyEndUserId=oeu1698071266316r0.8778444295933242; pjs-last-visited-page=/rental-manager/post-a-listing/; pjs-pages-visited=1; _cs_c=0; __stripe_mid=9e8d08b8-2188-4f32-884f-0585fb1a8fa2855b24; _cs_id=13550948-576d-a577-ab58-49230338e93a.1698071269.1.1698071269.1698071269.1.1732235269580; _px3=98e253be48bfc0a4c0f1c2e90b890b54a512a958ff686ee2c0e16f51381421c3:kk73nZ/YzypMsFQmBYbbNqf97K99+jen2gtDWUtgzRL9JvAUrz3tIQD12JeeU8OeZRtrjdfbaLiR2N5tqKQ9jA==:1000:8dfTVGJ5TCJvpjbuajqWrQzeNiPZS15I8NJ7SwIWFXq/tMFGxVpM8PIJQZ02+mbVGERo1V4cgAbDTLEjdkb/bYlDwSRDGV0W9B5Y2zL8iGO+LJqRnh9dNOcOE1DoneSuD5GVVJaLDIDlhGjVSFEEB+kXBN12UKO62YFeNg3G5cehS5wEA+GtBBhSmrQWE/+DAs73OM+QSXdX0OO9Hz6po/NuMD6AVbGeyZPJerstnMI=; _clsk=fnq95p|1698219178535|9|0|d.clarity.ms/collect; _gid=GA1.2.2113524659.1698219066; _uetsid=79bbdc70730811ee8bb81dbdce9a5d4b; _uetvid=aa920fe070d311ee8796c936ffe8c925; tfpsi=59080175-a4f8-45b0-924b-efb3bc2bddd8; g_state={"i_p":1698226347544,"i_l":1}'
          }

Realty = namedtuple('Realty', 'address price url')

def main():
    """ main function """
    realties = set()
    page = 0
    while True:
        time.sleep(1)
        page += 1
        # if page > 1: break
        
        params = {
                'searchQueryState': {
                        # 'mapBounds':{'north': 37.97, 'east': -121.614, 'south': 37.59, 'west': -123.4},
                        # 'regionSelection':[{'regionId': 20330,'regionType': 6}],
                        # 'isMapVisible': True,
                        'filterState': {'price': {'max': 525671},
                                        'beds': {'min': 1},
                                        'isForSaleForeclosure': {'value': False},
                                        'monthlyPayment': {'max': 3000, 'min': 2800},
                                        'isAllHomes': {'value': True},
                                        'isAuction': {'value': False},
                                        'isNewConstruction': {'value': False},
                                        'isForRent': {'value': True},
                                        'isForSaleByOwner': {'value': False},
                                        'isComingSoon': {'value': False},
                                        'isForSaleByAgent': {'value': False}
                                        },
                        # 'isListVisible': True,
                        'pagination': {'currentPage': page},
                }
        }
        request_params = urllib.parse.urlencode(params)
        response = requests.get(base_url, headers=header, params=request_params)
        
        if response.status_code != 200:
            break

        # # parsing current url for real page number
        # params_data = parse_qs(urlparse(response.url).query)
        # params_data = params_data.get('searchQueryState', ["""{'pagination': {'currentPage': None}}"""])
        # params_data = eval(params_data[0])
        # current_page = params_data.get('pagination').get('currentPage')
        # if current_page is None:
        #     break

        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        page_number_element_list = soup.find_all('li', class_='PaginationNumberItem-c11n-8-84-3__sc-bnmlxt-0 cA-Ddyj')
        obtainable_pages = set()
        for page_number_element in page_number_element_list:
            page_number_data = page_number_element.find('a')
            obtainable_pages.add(int(page_number_data.text))

        if page not in obtainable_pages: # all pages were scraped
            break

        items_list = soup.find('ul', class_='List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards')
    #     # items_list = soup.find_all('li', class_='ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl')
        print(f'Scraping page # {page}, {len(items_list)} records found')
        items_list = soup.find('ul', class_='List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards')
        for i, item in enumerate(items_list):
            script_element = item.find('script', {'type' : 'application/ld+json'})
            price_element = item.find('span', {'data-test': 'property-card-price',
                                               'class': 'PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr'})
            if not script_element or not price_element:
                continue
            script_data = json.loads(script_element.contents[0])
            item_url = script_data.get('url')
            if "http" not in item_url:
                item_url = f"https://www.zillow.com{item_url}"
            item_address = script_data.get('name')
            price_data = re.search(r'\$\d\,\d{3}', price_element.text)[0]
            item_price = int(re.sub(r'[^\d.]', '', price_data))
            realties.add(Realty(item_address, item_price, item_url))

    # print(*realties, sep='\n--------------------\n')
    print(f'{len(realties)} properties were found') 
    realties = list(realties)
    workbook = xlsxwriter.Workbook(EXCELFILE)
    worksheet = workbook.add_worksheet()
    # write names of columns
    for column, field_name in enumerate(realties[0]._fields):
        worksheet.write(0, column, field_name)
    # write data
    for row, realty in enumerate(realties, 1):
        for column, value in enumerate(realty):
            worksheet.write(row, column, value)
    workbook.close()

if __name__ == "__main__":
    import os
    import sys
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()

