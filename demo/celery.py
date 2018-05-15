#!/usr/bin/env python
from __future__ import absolute_import

from celery import Celery
from .celery_config import CeleryConfig

app = Celery('demo')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object(CeleryConfig)

if __name__ == '__main__':

    # Use raven_config
    try:
        from .celery_config import RAVEN_CONFIG
    except ImportError:
        RAVEN_CONFIG = None
    if RAVEN_CONFIG:
        from raven import Client
        from raven.contrib.celery import register_signal

        # Celery signal registration
        raven_client = Client(dsn=RAVEN_CONFIG['dsn'])
        register_signal(raven_client)

    # Use logging config
    try:
        from .celery_config import LOGGING
    except ImportError:
        LOGGING = None

    if LOGGING:
        from logging.config import dictConfig
        dictConfig(LOGGING)

    app.start()
