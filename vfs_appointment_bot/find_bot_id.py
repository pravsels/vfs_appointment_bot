import requests 
from _ConfigReader import _ConfigReader

_config_reader = _ConfigReader()
_section_header = "TELEGRAM"
bot_token = _config_reader.read_prop(_section_header,"bot_token")

print('bot token : ', bot_token)
url = f"https://api.telegram.org/bot{bot_token}/getUpdates"

print('JSON : ', requests.get(url).json())

