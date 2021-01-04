import requests
base_url = "https://rest.coinapi.io/v1/exchangerate/"
headers = {'X-CoinAPI-Key' : 'YOURKEYHERE'}

def exchange_rate(TYPE,FROM): #TYPE為對象, FROM為被換者
    url = base_url+FROM+"/"+TYPE
    data = requests.get(url,verify=False,headers=headers)
    data = data.json()
    return data['rate']
