import configparser
import os
from unittest.mock import patch

# 默认配置来自 INI，再让环境中的同名值覆盖。
config = configparser.ConfigParser()
config.read_string("[sync]\nretries = 2\n")

with patch.dict(os.environ, {"SYNC_RETRIES": "4"}):
    raw = os.getenv("SYNC_RETRIES", config["sync"]["retries"])
    print(int(raw))
