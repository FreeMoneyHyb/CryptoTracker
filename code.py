import random
import datetime 
import requests
import pycoingecko
from datetime import date 
from pycoingecko import CoinGeckoAPI

print("Loading")
cg = CoinGeckoAPI()
today = date.today()

print(f'''
  ___________________
  Crypto PROJECT v1.1.0
  
  1 = crypto price | 2 = coin lookup
  
  
  
  
  Date: {today}
''')
menu = input("Enter Somthing : ")
if menu =="1":
  btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
  eth = cg.get_price(ids='ethereum', vs_currencies='usd')  
  ltc = cg.get_price(ids='litecoin', vs_currencies='usd')  
  doge = cg.get_price(ids='dogecoin', vs_currencies='usd')  
  xmr = cg.get_price(ids='monero', vs_currencies='usd')    
  print(f'''
  {btc}
  {eth}
  {ltc}
  {doge}
  {xmr}
   ''')
elif menu =='2':
  coin69 = input('Enter The FULL Name Of The Coin : ')
  mcoin = cg.get_price(ids=f'{coin69}', vs_currencies='usd')    
  print(f'''Here You Go Friend --->> {mcoin} 
  
NOTE : If empty coin {coin69} not found''')
