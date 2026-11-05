from threading import Lock, Thread

total = 0
lock = Lock()


def count():
    global total
    for _ in range(1000):
        # 把读、加、写作为一段受保护的操作。
        with lock:
            total += 1


workers = [Thread(target=count) for _ in range(2)]
for worker in workers:
    worker.start()
for worker in workers:
    worker.join()
print(total)
