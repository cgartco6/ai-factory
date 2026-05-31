import redis
from rq import Queue
from backend.config import REDIS_URL


conn = redis.from_url(REDIS_URL)
queue = Queue(connection=conn)


def enqueue(task, *args):
    return queue.enqueue(task, *args)
