import requests

api = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

GET = requests.get(api)

FORMAT = GET.json()

HIGH = FORMAT['USDBRL']['high']

LOW = FORMAT['USDBRL']['low']

print('O valor de 1 dollar mais alto atualmente é: {} reais '.format(HIGH))
print('o valor de 1 dollar mais baixo atualmente é: {} reais'.format(LOW))
