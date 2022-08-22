# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process, Pool


def print_name(name, i):
    print(
        f"Run child process {name}_{i}, pid: {os.getpid()}, my parent pid is: {os.getppid()}..."
    )
    print(f"My name is: {name}")
    time.sleep(10)


def main1():
    print(f"Parent process pid: {os.getpid()}.")
    for i in range(4):
        print_name("liyifei", i)
    print("Waiting for all subprocesses done...")
    print("All subprocesses done.")


if __name__ == "__main__":
    main1()
