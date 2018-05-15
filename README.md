
# This is Celery 4.0 proof of concept

## Run demo

1. Install Celery (from `requirements.txt`).
 
    ```bash
    pip install -r requirements.txt
    ```

2. Start redis (on port 6379).

3. Start `run-worker.sh` (in root directory) in one terminal. 

4. run `use_celery_tasks.py` in second terminal. Watch the result


## Add custom tasks

1. Create some tasks (in `tasks.py`) as modules

2. Call your tasks from code.

## License

License: WTFPL || 2BSD
