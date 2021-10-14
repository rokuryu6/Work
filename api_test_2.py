import requests
from random import randint
import random
from datetime import date, datetime

from config import *

# Рандомное число для ID Инцидента
rand_id = randint(8020, 8040)
# Дата и время создания инцидента (текущая)
current_date = date.today()
current_time = datetime.now().time()
# Рандом для приоритета инцидента
priority_list = ["1", "2", "3", "4"]
random_priority = random.choice(priority_list)
# UseCase
usecase_list = ['LogSourceTime', 'Source IP', 'Source Name', 'Destination IP', 'Destination Name', 'User Name', 'Rule Name', 'QRadarAlertTime', 'Category Name', 'Source Network', 'Destination Network', 'stand', 'ATT&CK', 'Additional', 'URL Incident Link', 'Sentinel incident ID']
UseCase = random.choice(usecase_list)
# Рандомная строка для ресурсов и пользователей
rand = randint(1, 21)
rend_str = str(rand)

# Тест 1. Отправка инцидента из Jira SOC
def create_incident():
    url = f'{BASE_URL}/api/v1/Incidents'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'secret_key': S_KEY}
    # Готовый ID конкретной организации ООО "Ромашка"
    id_str = f"ром-{str(rand_id)}"
    data = {
        "summary": f'АвтоТест-{str(rand_id)}',
        "key": id_str,
        "created": f"{str(current_date)}T{str(current_time)}+0300",
        "IncidentStartTime": "",
        "QRadarAlertTime": "2018-01-01T01:00:00.0+0300",
        "LogSourceTime": "",
        "Priority": random_priority,
        "SourceIP": "IP источника",
        "Destination IP": "IP назначения",
        "Username": f'Имя пользователя{str(rend_str)}',
        "Source Hostname": f'Source host{str(rend_str)}',
        "Destination Hostname": f'Destination host{str(rend_str)}',
        "Rule Name": "Название правила",
        "Cause": "Причина",
        "Category Name": "Спам",
        "Source Network": "Source Network",
        "Destination Network": "Destination Network",
        "stand": "other",
        "Solution": "Решение автоматическое закрытие",
        "Additional": "Дополнительная информация",
        "Description": "Описание",
        "ATT&CK": "ATT&CK Matrix Tactics",
        "UseCase": UseCase,
        "assignee": {
            "user_name": "имя аналитика",
            "login":"k.kuzina"},
        "URL Incident Link": "10.5.200.124:8443/issues",
        "Sentinel incident ID": "999",
        "responsible client": {
            "user_name": "",
            "login": "логин пользователя"},
        "SLA": {
            "ACCWork": {
                "elapsedTime": 42572,
                "remainingTime": 1157428,
                "goalDuration": 1800000},
                "Reg_incident": {
                    "elapsedTime": 85000078,
                    "remainingTime": 2000022,
                    "goalDuration": 2600000}
        }
    }

    response = requests.post(url, json=data, headers=headers)
    return response


# Отправка комментария из jira SOC

def create_comment():
    url = f'{BASE_URL}/api/v1/Incidents/comment'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'secret_key': S_KEY}
    # Готовый ID конкретной организации ООО "Ромашка"
    id_str = f"ром-{str(rand_id)}"
    data = {
        "key": id_str,
        "coment.body": "комент API_test",
        "autor":
            {"user_name": "",
             "login": "k.kuzina"}
        }

    response = requests.post(url, json=data, headers=headers)
    return response
