
# Celery setting
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/1'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERYD_CONCURRENCY = 2
CELERYD_MAX_TASKS_PER_CHILD = 5



# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'web', 'celery']
ROOT_URLCONF = 'titanic_project.urls'


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'titanic_project.views': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'titanic_project.task': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'titanic_project.model': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
