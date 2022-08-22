# -*- coding:utf-8 -*-
import time
import os
import threading
from multiprocessing.pool import ThreadPool


# 子线程要执行的代码
def run_thread(name):
    print(
        f"Run child thread {name}, pid: {os.getpid()}, my parent pid is: {os.getppid()}..."
    )
    print(
        f"Run child thread {name}, thread pid: {threading.get_ident()}, my parent thread pid is: {threading.main_thread().ident}..."
    )
    # time.sleep(60)


def main():
    print(f"Parent process pid: {os.getpid()}, my thread pid: {threading.get_ident()}")
    t = threading.Thread(target=run_thread, args=("liyifei",))
    t.start()
    t.join()


if __name__ == "__main__":
    main()
