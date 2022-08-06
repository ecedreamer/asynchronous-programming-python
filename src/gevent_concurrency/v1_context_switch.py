import gevent


def service1():
    print('Running service1')
    gevent.sleep(2)
    print('Remaining task of service1')

def service2():
    print('Running Service2')
    gevent.sleep(4)
    print('Remaining task of service2')


def main():
    gevent.joinall([
        gevent.spawn(service1),
        gevent.spawn(service2),
    ])


if __name__ == "__main__":
    main()