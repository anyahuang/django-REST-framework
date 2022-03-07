import requests 
import secret
import pprint as pp
# pprint is pretty print , makes it easier to read

def get_price(id):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': secret.API_KEY,}

        parameters = {
            'id':id
          }
        # r is short for response    
        r = requests.get(url, params=parameters, headers=headers)

        # build up a class so we can easily make the REST API call

        class CMC:
            def __init__(self, token):
                pass
            
        cmc = CMC(secret.API_KEY)    

        name = (r.json().get('data').get(id).get('name'))

        price = (r.json().get('data').get(id).get('quote').get('USD').get('price'))
        return f" One {name} is now {price} USD"      

response = input(f"insert 1 if you wanna know the price of Bitcoin , 1027 for Ethereum, and 2 for Litecoin: ")   
print(get_price(response))
