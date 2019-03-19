# coding:utf-8
import time
import threading
# import os


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
    loop0()
    loop1()
    print("all done at:", time.ctime())


if __name__ == '__main__':
    main()
