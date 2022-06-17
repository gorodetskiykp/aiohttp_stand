from config_model import MainConfig
from settings import BASE_DIR


DEFAULT_CONFIG_PATH = BASE_DIR / 'conf'

def load_config(config_file):
    with open(DEFAULT_CONFIG_PATH / config_file, 'r') as config_file:
        return MainConfig.parse_raw(config_file.read())