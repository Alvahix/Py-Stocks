from iexfinance import get_market_tops
from iexfinance import get_available_symbols
from time import *
import csv



m = strftime('%H%M')
m_int = int(m)
greet = 'Hello'
when = 'day'
if 0000 <= m_int <= 1159:
    greet = 'Good morning,'
    when = 'day'
elif 1200 <= m_int <= 1659:
    greet = 'Good afternoon,'
    when = 'day'
elif 1700 <= m_int <= 2359:
    greet = 'Good evening,'
    when = 'evening'

# debugging
# print(type(sym)) = 'list'
# length of list = 8674
print(greet + ' I\'m I.D.A., Integrated Developing Assistant. This is the stock edition of me. Which stock would you like me to look up?')
while True:
    stock = input()
    stock = stock.upper()
    if stock in ['no', 'No', 'NO']:
        break

    csv_file = csv.reader(open('symbols.csv', 'r'), delimiter=',')

    for row in csv_file:
        if stock in row[0]:
            print('\n')
            print('Corporation Name:', row[1])
    else:
        stocks_all_info = get_market_tops(stock)
        stocks_all_info_unpack = stocks_all_info[0]  # have to unpack the {} from inside the []
        print('Stock Symbol:', stocks_all_info_unpack['symbol'])
        print('Last Sale Price: $' + str(stocks_all_info_unpack['lastSalePrice']))
        print('Market Percent for ' + stocks_all_info_unpack['symbol'] + ': ' + str(stocks_all_info_unpack['marketPercent']) + '%')
        print('Market Volume for ' + stocks_all_info_unpack['symbol'] + ': ' + str(stocks_all_info_unpack['volume']))
        print('\n')
        print('Is there any other stock I can look up for you? If no, simply type \"no\"')

print('\n')
print('Thanks for using I.D.A. stock edition. Have a nice ' + when + '!')



