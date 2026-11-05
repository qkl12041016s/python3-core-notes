"""用队列与线程下载明确给定的一组资源。"""
import argparse
import json
from pathlib import Path
from queue import Queue
from threading import Thread

import requests


def download_all(urls, output, workers=2):
    # 索引决定输出名与结果顺序，工作线程各用一个 Session。
    if workers < 1:
        raise ValueError("workers 必须大于零")
    urls = tuple(urls)
    output.mkdir(parents=True, exist_ok=True)
    tasks, results = Queue(), Queue()
    for index, url in enumerate(urls, start=1):
        tasks.put((index, url))
    for _ in range(workers):
        tasks.put(None)

    def work():
        with requests.Session() as session:
            while True:
                item = tasks.get()
                try:
                    if item is None:
                        return
                    index, url = item
                    final = output / f"{index:03d}.bin"
                    temporary = final.with_suffix(".part")
                    try:
                        if final.exists():
                            raise FileExistsError(f"目标已存在：{final.name}")
                        with session.get(url, timeout=5, stream=True) as reply:
                            reply.raise_for_status()
                            with temporary.open("wb") as stream:
                                for chunk in reply.iter_content(65536):
                                    stream.write(chunk)
                        temporary.replace(final)
                        results.put((index, True, final.name))
                    except (requests.RequestException, OSError) as error:
                        message = str(error)
                        try:
                            temporary.unlink(missing_ok=True)
                        except OSError as cleanup_error:
                            message += f"；临时文件清理失败：{cleanup_error}"
                        results.put((index, False, message))
                finally:
                    tasks.task_done()

    threads = [Thread(target=work) for _ in range(workers)]
    for thread in threads:
        thread.start()
    tasks.join()
    for thread in threads:
        thread.join()
    return sorted(results.get() for _ in range(len(urls)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    urls = [line.strip() for line in args.urls.read_text(encoding="utf-8").splitlines() if line.strip()]
    results = download_all(urls, args.output)
    # 保留失败信息，由调用方决定是否重试。
    print(json.dumps(results, ensure_ascii=False))
    return 0 if all(ok for _, ok, _ in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
