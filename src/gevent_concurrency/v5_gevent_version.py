from gevent import monkey
monkey.patch_all()
import time
import gevent
import requests


def io_bound_task(url="https://google.com"):
    resp = requests.get(url)
    return resp.status_code


def io_bound_task1(delay=None):
    while True:
        result = [io_bound_task(url="https://python.org") for _ in range(2)]
        print(time.time(), "TASK-1", result[0], result[-1])
        print(f"{time.time()} :: TASK-1 and sleeping for {delay} seconds")
        gevent.sleep(delay) # Non blocking IO bound 
    
def io_bound_task2(delay=None):
    while True:
        result = [io_bound_task(url="https://go.dev") for _ in range(2)]
        print(time.time(), "TASK-2", result[0], result[-1])
        print(f"{time.time()} :: TASK-2 and sleeping for {delay} seconds")
        gevent.sleep(delay) # Non blocking IO bound 


def main():
    print("Starting.................")
    t1 = gevent.spawn(io_bound_task1, 2)
    t2 = gevent.spawn(io_bound_task2, 4)
    gevent.joinall([t1, t2])


if __name__ == "__main__":
    main()
