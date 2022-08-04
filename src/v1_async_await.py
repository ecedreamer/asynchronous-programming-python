import asyncio
import time


async def io_bound_task(arg=None):
    await asyncio.sleep(1) # Non blocking IO bound task
    return bool(arg)


async def main():
    print("Starting.................")
    t1 = time.time()
    ping1 = await io_bound_task("dipak")
    ping2 = await io_bound_task()
    ping3 = await io_bound_task()
    ping5 = await io_bound_task(5)
    ping6 = await io_bound_task()
    t2 = time.time()
    print("Ending...................")
    print("output: ", ping1, ping2, ping3, ping5, ping6)
    print("Time taken:", t2-t1)


if __name__ == "__main__":
    asyncio.run(main())


""" 
=================== OUTPUT ===================

Starting.................
Ending...................
output:  True False False True False
Time taken: 5.006279945373535

"""