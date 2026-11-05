# 修复版。
import asyncio

async def main():
    # 在当前循环内等待，不另开一个循环。
    await asyncio.sleep(0)
    print("ready")

asyncio.run(main())
