#!/usr/bin/env python3
import requests

TOKEN = ''
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'https://10.10.1.10:1080',
# }
#
# r = requests.get(f'{MAIN_URL}/getUpdates', proxies=proxies)

# # ответ
# payload = {
#     'chat_id': 1111,
#     'text': 'Hello',
#     'reply_to_message_id': 1
# }
#
# r = requests.post(f'{MAIN_URL}/sendMessage', data=payload)

# получение данных
r = requests.get(f'{MAIN_URL}/getUpdates')

print(r.json())
