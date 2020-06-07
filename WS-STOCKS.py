
import requests
from bs4 import BeautifulSoup
symbol = input("ENTER THE COMPANY SYMBOL/CODE =")
url =('https://finance.yahoo.com/quote/') + symbol + ('/history?p=') + symbol
text = requests.get(url)
soup = BeautifulSoup(text.content,"html.parser")
#print('DATE         OPEN   HIGH   LOW    CLOSED    ')
#print('FOR PRESENT STOCKS USE CODE 51 AND FOR PREVIOUS STOCK INCREMENT IT BY 15 ')
print('ENTER THE NUMBER OF PREVIOUS DAYS FROM TODAY (FOR TODAYS STOCK PRESS 1 , FOR YESTERDAY STOCK PRESS 2)=')
O = 36
D = int(input())
def stock_price():
  date = soup.find_all('span',{'data-reactid' : O+(15*D) })[0].text
  open_price = soup.find_all('span',{'data-reactid' : O+2+(15*D) })[0].text
  high_price = soup.find_all('span',{'data-reactid' : O+4+(15*D) })[0].text
  low_price = soup.find_all('span',{'data-reactid' : O+6+(15*D) })[0].text
  close_price = soup.find_all('span',{'data-reactid' : O+8+(15*D) })[0].text
  print(date,open_price,high_price,low_price,close_price,end = "    ")

stock_price()