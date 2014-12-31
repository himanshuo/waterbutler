import os
import json
import logging


PROJECT_NAME = 'waterbutler'
PROJECT_CONFIG_PATH = '~/.cos'


try:
    config_path = os.environ['{}_CONFIG'.format(PROJECT_NAME.upper())]
except KeyError:
    env = os.environ.get('ENV', 'test')
    config_path = '{}/{}-{}.json'.format(PROJECT_CONFIG_PATH, PROJECT_NAME, env)


config = {}
config_path = os.path.expanduser(config_path)
if not os.path.exists(config_path):
    logging.warn('No \'{}\' configuration file found'.format(config_path))
else:
    with open(os.path.expanduser(config_path)) as fp:
        config = json.load(fp)


OSFSTORAGE_PROVIDER_CONFIG = config.get('OSFSTORAGE_PROVIDER_CONFIG')
SERVER_CONFIG = config.get('SERVER_CONFIG')
