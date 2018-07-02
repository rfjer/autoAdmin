from .settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "devops",
        'USER': 'root',
        'PASSWORD': "123456",
        'HOST': "127.0.0.1",
        'OPTIONS': {
            'init_command': "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'"
        }
    },
   # "zabbix": {
   #     'ENGINE': 'django.db.backends.mysql',
   #     'NAME': "zabbix",
   #     'USER': 'zabbix',
   #     'PASSWORD': "zabbix",
   #     'HOST': "192.168.20.116",
   #     'OPTIONS': {
   #         'init_command': "SET storage_engine=INNODB;SET sql_mode='STRICT_TRANS_TABLES'"
   #     }
   # }
}
LOGGING = {}