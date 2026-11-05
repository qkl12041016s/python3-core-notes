import asyncio


async def check(name, delay):
    # 等待时让出事件循环，其他任务可以继续。
    await asyncio.sleep(delay)
    print("完成", name)
    return name


async def main():
    # gather 按传入顺序返回各自结果。
    results = await asyncio.gather(
        check("slow", 0.05),
        check("fast", 0.0),
    )
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
