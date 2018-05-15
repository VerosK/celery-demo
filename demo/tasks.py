from __future__ import absolute_import, unicode_literals

from .celery import app

import time
import requests

@app.task(name='demo.my_address', bind=True)
          # unique name                # add self
def get_my_address(self):
    response = requests.get('http://httpbin.org/ip')
    parsed = response.json()
    assert type(parsed) == dict, type(parsed)
    return parsed['origin']


@app.task(name='sleep_task', bind=True, ignore_result=True)
                                        # We don't need results of this task
def sleep_task(self):
    time.sleep(10)


