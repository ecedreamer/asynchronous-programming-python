import asyncio


async def service1():
    print('Running service1')
    await asyncio.sleep(2)
    print('Remaining task of service1')

async def service2():
    print('Running Service2')
    await asyncio.sleep(4)
    print('Remaining task of service2')


async def main():
    await asyncio.gather(service1(), service2())


if __name__ == "__main__":
    asyncio.run(main())