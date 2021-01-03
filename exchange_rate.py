import requests
base_url = "https://rest.coinapi.io/v1/exchangerate/"
headers = {'X-CoinAPI-Key' : '4DD30C3D-65FF-43B4-9309-51B6BE76FE16'}

def exchange_rate(TYPE,FROM): #TYPE為對象, FROM為被換者
    url = base_url+FROM+"/"+TYPE
    data = requests.get(url,verify=False,headers=headers)
    data = data.json()
    return data['rate']