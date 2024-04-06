import requests 
from _ConfigReader import _ConfigReader

_config_reader = _ConfigReader()
_section_header = "TELEGRAM"
bot_token = _config_reader.read_prop(_section_header,"bot_token")
chat_id = _config_reader.read_prop(_section_header,"chat_id")

message = "hello, human"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json()) 
