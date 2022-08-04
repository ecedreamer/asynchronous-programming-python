import asyncio
from concurrent.futures import ThreadPoolExecutor
import time


async def io_bound_task(arg=None):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, time.sleep, 1) # running blocking code in executor in coroutines
    ##  or simply 
    # await loop.run_in_executor(None, time.sleep, 1)
    return bool(arg)


async def main():
    print("Starting.................")
    t1 = time.time()
    result = await asyncio.gather(io_bound_task("dipak"), io_bound_task(), io_bound_task(), io_bound_task(5), io_bound_task())
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
output:  [True, False, False, True, False]
Time taken: 1.0037753582000732

"""