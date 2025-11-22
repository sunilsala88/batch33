








import requests
TOKEN = '8297174286:AAEkfGGHtB2yXyIhFYoP8PwI78aV98oXS3c'
ids = '5563890177'

message='this is my first message from python script'
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ids}&parse_mode=Markdown&text={message}"
print(requests.get(url).json())