'''
Com este script testamos nosso servidor (a Endpoint de predição) no Flask
'''
import requests

# Exemplo de solicitação de empréstimo
application = {
    "Term": 84,
    "NoEmp": 5,
    "CreateJob": 0,
    "RetainedJob": 5,
    "longitude": -77.9221,
    "latitude": 35.3664,
    "GrAppv": 1500000.0,
    "SBA_Appv": 1275000.0,
    "is_new": True,
    "FranchiseCode": "0",
    "UrbanRural": 1,
    "City": "Other",
    "State": "NC",
    "Bank": "BBCN BANK",
    "BankState": "CA",
    "RevLineCr": "N",
    "naics_first_two": "45",
    "same_state": False,
}

# Localização do servidor (server)
url = "http://0.0.0.0:8989/predict"

# Send request (Envio pedido)
resp = requests.post(url, json=application)

# Printamos o resultado
print('')
print("Nosso resultado de EMPRÉSTIMO será uma probabilidade: ")
print(resp.json())
