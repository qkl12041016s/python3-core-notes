import os

from dotenv import load_dotenv

# 显式加载 .env，不覆盖当前已经存在的环境变量。
load_dotenv(".env", override=False)
print(int(os.getenv("SYNC_RETRIES", "2")))
