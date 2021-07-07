from celery import Celery

app = Celery("tasks", broker="redis://redis")

@app.task
def add(x, y):
    return x + y
