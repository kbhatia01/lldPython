import asyncio
async def hello():
    print("hellopoooo")
    await asyncio.sleep(1)
    print('Hello World!')

async def func1():
    print("func1")


async def main():
    l = await asyncio.gather(hello(),
    func1())
    print(l)

asyncio.run(main())
