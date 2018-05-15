# Celery config



class CeleryConfig:
    broker_url = 'redis://localhost/0'  # tasks are stored here
    broker_transport_options = dict(
        visibility_timeout=6 * 3600,  # task will expire after 6 hours
        #  after data
    )

    result_backend = 'redis://localhost/1'  # tasks results are stored here
    result_expires = 86400  # tasks results expire after 24 hours,

    timezone = 'Europe/Prague'
    enable_utc = True
    task_default_queue = 'default'

    # add modules with tasks here (or use autodiscover)
    #           see http://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.autodiscover_tasks
    include = [
        'demo.tasks'
    ]

# RAVEN_CONFIG = ... config me

# LOGGING = ... use logging dictConfig here
