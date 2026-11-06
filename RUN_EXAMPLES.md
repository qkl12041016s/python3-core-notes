# 运行示例

先在独立虚拟环境中安装 `requirements-demo.txt`。第 3 至 17 章样例在 `examples/chXX`，从相应目录执行文件。

- 第 7 章运行 `python -m pytest -q`。`use_calc.py` 与 `calc.py` 需放在同目录。
- 第 8 章运行 `python -m black --check style_demo.py` 和 `python -m ruff check style_demo.py`。
- 第 10 章把 `.env.example` 复制为 `.env` 后运行 `load_env.py`。
- 第 11 章执行 `python scan_log.py --input sample.log`。
- 第 13 章 `local_http.py` 在本机启临时服务。`browser_demo.py` 需要 Selenium 和可用浏览器驱动。
- 第 14 章 `orm_note.py` 使用本地 SQLite。`external_databases.py` 需要实际测试库和相应环境变量。
- 第 15 章 `window_demo.py` 需要可显示窗口的桌面环境。
- 第 16 章 `draw_report.py` 在当前目录生成 `report.pdf`。
- 第 17 章构建样例包并换目录安装验证。Docker 示例需要已构建的 wheel 与 Docker。

## 四阶段项目

- 在 `projects/01-contacts` 运行 `python contacts.py --file demo.json add Xiaoxue 0000`，随后用 `update Xiaoxue 1234`、`list` 和 `remove Xiaoxue` 核对。
- 在 `projects/02-downloader` 准备一行一个 URL 的 `urls.txt`，运行 `python download.py --urls urls.txt --output downloads`。
- 在 `projects/03-report` 运行 `python report.py --input sample.csv --output result`。也可传入 `.xlsx` 文件，程序读取第一张工作表。结果目录应为新目录。
- 在 `projects/04-library`，路线 A 安装 `PyQt6` 后执行 `python gui.py`。
- 路线 B 运行 `python -m uvicorn api:create_app --factory`，再用本地 `/docs` 页面验证接口。

项目压缩包保留全部源码、样本与配置。需要额外服务或界面的程序请按正文运行条件复核。

## 本版验证记录

使用 Python 3.12 运行新增的 25 个章节样例，包括参数化测试。
本地验证了格式化与静态检查，以及 Git 的初始化、提交、分支和 diff。
通讯录、下载器、报表、资料存储和 FastAPI 测试覆盖正常与失败路径。
浏览器例子、外部 MySQL/MongoDB 客户端、Tkinter/PyQt 界面完成语法检查，
实际交互需要对应运行环境复核。Dockerfile 的构建和容器启动需要 Docker 环境。

## v1.1.0 新增示例

以下均在Python3.11+可运行，本轮实测Python3.12：

```sh
python examples/revision/modern_match.py
python examples/revision/exception_groups.py
python examples/revision/async_lifecycle.py
python examples/appendixA/inspect_install.py
```

uv命令是终端操作，不写入.py脚本。原始源文件是运行入口，PDF行号与折行箭头不属于Python语法。
