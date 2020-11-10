from django.conf import settings
import requests

token = settings.BOT_TOKEN
chat_id = settings.CHAT_ID
url = f'https://api.telegram.org/bot{token}/'


def send_notification(data):
    endpoint = f'{url}sendMessage'
    fields = {
        'chat_id': chat_id,
        'text': data.notification,
        'parse_mode': 'MARKDOWN'
    }
    requests.post(endpoint, fields)


def send_as_attachment(data):
    endpoint = f'{url}sendDocument'
    files = {'document': open(data.resume.path, 'rb')}
    fields = {
        'caption': data.notification,
        'chat_id': chat_id,
        'parse_mode': 'MARKDOWN'
    }
    requests.post(endpoint, files=files, data=fields)
