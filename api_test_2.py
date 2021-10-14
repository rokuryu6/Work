import requests
from random import randint
import random
from datetime import date, datetime

from config import *


rand_id = randint(8020, 8040)

current_date = date.today()
current_time = datetime.now().time()

priority_list = ["1", "2", "3", "4"]
random_priority = random.choice(priority_list)

usecase_list = ['LogSourceTime', 'Source IP', 'Source Name']
UseCase = random.choice(usecase_list)

rand = randint(1, 21)
rend_str = str(rand)

def create_incident():
    url = f'{BASE_URL}/api/...'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'secret_key': S_KEY}
    id_str = f"ром-{str(rand_id)}"
    data = {
        "summary": f'АвтоТест-{str(rand_id)}',
        "key": id_str,
        "created": f"{str(current_date)}T{str(current_time)}+0300",
        "Priority": random_priority,
        "Username": f'Имя пользователя{str(rend_str)}',
        "Source Hostname": f'Source host{str(rend_str)}',
        "Destination Hostname": f'Destination host{str(rend_str)}',
        "UseCase": UseCase}

    response = requests.post(url, json=data, headers=headers)
    return response

def create_comment():
    url = f'{BASE_URL}/api/v1/Incidents/comment'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'secret_key': S_KEY}
    id_str = f"ром-{str(rand_id)}"
    data = {
        "key": id_str}

    response = requests.post(url, json=data, headers=headers)
    return response
