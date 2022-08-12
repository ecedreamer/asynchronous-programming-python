import gevent
from gevent import monkey
monkey.patch_all()  # To see gevent context switch, comment/uncomment this line and run the code. 
import requests


def service1():
    print('First line of service1')
    resp = requests.get("https://google.com")
    print(resp.status_code, "------------")
    print('Second line of service1')
    gevent.sleep(2)
    print('Third line of service1')

def service2():
    print('First line of service2')
    print('Second line of service2')
    gevent.sleep(3)
    print('Third line of service2')



def main():
    gevent.joinall([
        gevent.spawn(service1),
        gevent.spawn(service2),
    ])


if __name__ == "__main__":
    main()