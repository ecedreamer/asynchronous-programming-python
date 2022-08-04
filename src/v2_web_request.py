import asyncio
import time
import aiohttp


async def io_bound_task(url="https://google.com"):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status


async def main():
    print("Starting.................")
    t1 = time.time()
    coroutines = [io_bound_task() for _ in range(50)]
    result = await asyncio.gather(*coroutines)
    t2 = time.time()
    print("Ending...................")
    print("output: ", result)
    print("Time taken:", t2-t1)


if __name__ == "__main__":
    asyncio.run(main())


""" 
=================== OUTPUT ===================

Starting.................
Ending...................
output:  [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
Time taken: 4.224328279495239

"""