import asyncio
import time
import aiohttp


async def io_bound_task(url="https://google.com"):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status


async def io_bound_task1(delay=None):
    while True:
        coroutines = [io_bound_task(url="https://python.org") for _ in range(2)]
        result = await asyncio.gather(*coroutines)
        print(time.time(), "TASK-1", result[0], result[-1])
        print(f"{time.time()} :: TASK-1 and sleeping for {delay} seconds")
        await asyncio.sleep(delay) # Non blocking IO bound 
    
async def io_bound_task2(delay=None):
    while True:
        coroutines = [io_bound_task(url="https://go.dev") for _ in range(2)]
        result = await asyncio.gather(*coroutines)
        print(time.time(), "TASK-2", result[0], result[-1])
        print(f"{time.time()} :: TASK-2 and sleeping for {delay} seconds")
        await asyncio.sleep(delay) # Non blocking IO bound 


async def main():
    print("Starting.................")
    t1 = asyncio.create_task(io_bound_task1(2))
    t2 = asyncio.create_task(io_bound_task2(4))
    await t1
    await t2


if __name__ == "__main__":
    asyncio.run(main())
