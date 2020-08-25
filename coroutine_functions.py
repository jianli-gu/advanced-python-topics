import asyncio


async def task():
    print("Hello")
    await asyncio.sleep(2)
    print("World")


asyncio.run(task())
