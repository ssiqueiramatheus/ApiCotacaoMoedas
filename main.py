import  requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

#Cotação do dolar
cotacao_dolar = cotacoes['USDBRL']['bid']
print("Cotação do dolar: "+cotacao_dolar)

#Cotação do Euro
cotacao_euro = cotacoes['EURBRL']['bid']
print("Cotação do Euro: "+cotacao_euro)

#Cotação do Bitcoin
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
print("Cotação do Bitcoin: "+cotacao_bitcoin)