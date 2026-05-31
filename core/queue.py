import redis
from rq import Queue
from config import REDIS_URL


redis_conn = redis.from_url(REDIS_URL)
queue = Queue(connection=redis_conn)


def enqueue(job_func, *args):
    return queue.enqueue(job_func, *args)
