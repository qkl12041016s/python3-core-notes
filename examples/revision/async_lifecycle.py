import asyncio


async def bounded_job(name, delay):
    try:
        async with asyncio.timeout(0.05):
            await asyncio.sleep(delay)
            return name, "ok"
    except TimeoutError:
        return name, "timeout"
    finally:
        # Real resources should be closed here or via async with.
        pass


async def main():
    async with asyncio.TaskGroup() as group:
        fast = group.create_task(bounded_job("fast", 0.005))
        slow = group.create_task(bounded_job("slow", 0.2))
    print(fast.result())
    print(slow.result())

    task = asyncio.create_task(asyncio.sleep(10))
    await asyncio.sleep(0)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("cancellation collected")


if __name__ == "__main__":
    asyncio.run(main())
