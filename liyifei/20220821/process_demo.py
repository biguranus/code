# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print(
        f"Run child process {name}, pid: {os.getpid()}, my parent pid is: {os.getppid()}..."
    )
    time.sleep(60)


def main():
    print(f"Parent process pid: {os.getpid()}.")
    p = Process(target=run_proc, args=("liyifei",))
    print("Child process will start...")
    p.start()
    p.join()
    print("Child process end.")


if __name__ == "__main__":
    main()
