# coding:utf-8
import time
import threading
# import os
from multiprocessing import Pool


def loop0():
    print("start loop 0 at:", time.ctime())
    time.sleep(4)
    print("loop 0 done at:", time.ctime())


def loop1():
    print("start loop1 at:", time.ctime())
    time.sleep(2)
    print("loop 1 done at:", time.ctime())


def main():
    print("starting at:", time.ctime())
    # for i in range(5):#将要进行多任务的函数,不要使用for循环
    loop0()
    # loop1()
    print("all done at:", time.ctime())


if __name__ == '__main__':
    p = Pool(5)
    for i in range(5):
        p.apply_async(main, ())
    p.close()
    p.join()

