import asyncio
import time
import requests


def ping_google(url="https://google.com"):
    resp = requests.get(url)
    return resp.status_code


async def io_bound_task(arg=None):
    loop = asyncio.get_running_loop()
    status_code = await loop.run_in_executor(None, ping_google, "https://google.com")
    return status_code


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
output:  [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
Time taken: 14.795426368713379

"""