from dash import Dash
import pandas as pd
import requests
import json
from token import token

api_root = "https://brapi.dev/api/quote/"

def main():
    stocks = ['PETR4F']
    stocks.append('MGLU3')

    params = {
        "token" : token
    }
    
    for stock in stocks:
        r = requests.get(api_root + stock, params = params)
        
        data = json.loads(r.text)['results'][0]
        print(f"{data['symbol']} : {data['regularMarketPrice']}")

if __name__ == "__main__":
    main()