# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process, Pool


def print_name(name, i):
    print(
        f"Run child process {name}_{i}, pid: {os.getpid()}, my parent pid is: {os.getppid()}..."
    )
    print(f"My name is: {name}")
    time.sleep(60)


def main1():
    print(f"Parent process pid: {os.getpid()}, my ppid is : {os.getppid()}")
    p = Pool(4)
    for i in range(4):
        p.apply_async(func=print_name, args=("liyifei", i))
    print("Waiting for all subprocesses done...")
    p.close()
    p.join()
    print("All subprocesses done.")


if __name__ == "__main__":
    main1()
