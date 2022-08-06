from gevent.monkey import patch_all
patch_all()
import gevent
import requests
import time


def io_bound_task():
    return requests.get("https://python.org").status_code

def main():
    print("Starting.................")
    t1 = time.time()
    tasks = [gevent.spawn(io_bound_task) for _ in range(100)]
    result = gevent.joinall(tasks)
    t2 = time.time()
    print(result, t2-t1)

if __name__ == "__main__":
    main()