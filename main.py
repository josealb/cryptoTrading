import time
from bittrex.bittrex import Bittrex, API_V2_0
with open('my.keys', 'r') as myfile:
    api_key = myfile.readline().rstrip()
    api_secret = myfile.readline().rstrip()
import json

my_bittrex = Bittrex(api_key, api_secret)#, api_version=API_V2_0)
#print my_bittrex.get_balance('BTC')
#print my_bittrex.get_candles('BTC-ETH','oneMin')
#print my_bittrex.get_latest_candle('BTC-ETH','oneMin')
#print my_bittrex.get_ticker('BTC-ETH')

# Market to trade at
trade = 'BTC'
currency = 'ETH'
market = '{0}-{1}'.format(trade, currency)
# Amount of coins to buy
amount = 100
# How big of a profit you want to make
multiplier = 1.1

# Getting the BTC price for ETH
dogesummary = my_bittrex.get_marketsummary(market)
dogeprice = dogesummary['result'][0]['Ask']
print 'The price for {0} is {1:.8f} {2}.'.format(currency, dogeprice, trade)

while(True):
    #candle = my_bittrex.get_latest_candle('BTC-ETH','oneMin')
    #print candle[0]['close']
    #for key,val in candle.items():
    #    print key, "=>", val
    dogesummary = my_bittrex.get_marketsummary(market)
    dogeprice = dogesummary['result'][0]['Ask']
    print 'The price for {0} is {1:.8f} {2}.'.format(currency, dogeprice, trade)
    time.sleep(1)
