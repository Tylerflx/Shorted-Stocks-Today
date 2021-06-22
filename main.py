# this is practice for webscraping python
#this program I will try to scrape yahoo financial website for the most shorted stocks category
from bs4 import BeautifulSoup
import requests
import time
from short_stock import scrape_shortstocks

html_text = requests.get('https://finance.yahoo.com/u/yahoo-finance/watchlists/stocks-with-the-highest-short-interest').text
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('table', class_ = 'cwl-symbols W(100%)')
table_body = table.find('tbody')
table_data = table_body.find_all('tr')

if __name__ == '__main__':
    scrape_shortstocks(table_data)
    #can add loop to check every 10 mins
    # time_wait = 10
    # print(f'Updating in {time_wait} minutes')
    # time.sleep(time_wait * 60)