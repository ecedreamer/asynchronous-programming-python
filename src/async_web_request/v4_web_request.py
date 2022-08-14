import asyncio
import aiohttp


async def service1():
    print('First line of service1')
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as response:
            print(response.status)
    print('Second line of service1. Now sleeping for 2 s')
    await asyncio.sleep(2)
    print('Third line of service1')

async def service2():
    print('First line of service2')
    print('Second line of service2 Now sleeping for 3 s')
    await asyncio.sleep(3)
    print('Third line of service2')



async def main():
    t1 = asyncio.create_task(service1())
    t2 = asyncio.create_task(service2())
    await t1
    await t2


if __name__ == "__main__":
    asyncio.run(main())