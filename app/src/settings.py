import sys
import json

PATH_TO_CONFIG_FILE = sys.path[0]+'\\config.json'

def get_config_dict():
    with open(PATH_TO_CONFIG_FILE, 'r', encoding='utf-8') as config_file:
        return json.loads(config_file.read())


class Settings:
    @property
    def config_dict(self):
        return get_config_dict()
    
    @property
    def token(self):
        return self.config_dict['TOKEN']

settings=Settings()

