import random
import time

import datetime 
import requests
import pycoingecko

from datetime import date 
from pycoingecko import CoinGeckoAPI

print("[!] Loading")
cg = CoinGeckoAPI()
today = date.today()

print(f'''
  ___________________
  Crypto PROJECT v1.1.0
  
  1 = crypto price | 2 = coin price lookup
  
  3 = coin data search (all of it) | 4 = coin price tracker
  
  
  
  
  
  Date: {today}
''')
menu = input("[?] Enter Number : ")
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
  coin69 = input('[?] Enter The FULL Name Of The Coin : ')
  mcoin = cg.get_price(ids=f'{coin69}', vs_currencies='usd')    
  print(f'''Here You Go Friend --->> {mcoin} 
                        
NOTE : If empty coin {coin69} not found''')
elif menu =='3':
  name40 = input('[?] Enter The FULL Name Of The Coin : ')
  print("[!] this wont be pretty i mean it")
  time.sleep(2)
  mm = requests.get(f"https://api.coingecko.com/api/v3/coins/{name40}?localization=false")
  if mm.status_code == 200:
    print(mm.text)
  if mm.status_code == 404:    
    print("Coin not found")
elif menu =='4':
  name43 = input('[?] Enter The FULL Name Of The Coin : ')
  nummie = "999999999999"
  start = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={name43}&vs_currencies=usd%2Ceur')     
  nummie2 = int(nummie)
  for i in range (nummie2):
    choices = (['---','===','+++','~~~',])
    r = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={name43}&vs_currencies=usd%2Ceur')     
    if r.status_code == 200:
      time.sleep(.1)
      effect = random.choice(choices)     
      print(f'''
       Starting Prices {start.text}
       {effect}{effect}{effect}{effect}{effect}{effect}{effect}{effect}
       Current  Prices {r.text}
      ''')
