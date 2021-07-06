import requests  # работа с ответами json
import json
import random

J = {json}

url = 'http:...'
headers = {'Content-type': 'application/json',
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8',
           'secret_key': '...'}
data = J

answer = requests.post(url, data=json.dumps(data), headers=headers)
print(answer)
response = answer.json()
print(response)

f = open('report.txt', 'w', encoding="utf-8") #Запись в файл
f.write('ТЕСТ 1. Загрузка инцидента на портал через внешнее API \n' + str(answer) + '\n' + str(response) + '\n' + '\n')
f.close()

J = { json }

url = 'http://...'
headers = {'Content-type': 'application/json',  # Определение типа данных
           'Accept': 'text/plain',
           'Content-Encoding': 'utf-8',
           'secret_key': '...'
           }
data = J

answer = requests.post(url, data=json.dumps(data), headers=headers)
print(answer)

req = ''

if answer.status_code != 200:
    req = str(answer.json()) + '\n'

f = open('report.txt', 'a', encoding="utf-8") #Запись в файл
f.write('ТЕСТ 2. Отправка комментария через внешнее API \n' + str(answer) + '\n' + str(req) + '\n')
f.close()
