import os
import subprocess


def cls():
    print("\033[H\033[J", end="")


def exe(command):
    p = subprocess.call(command)

    if p == 0:
        print(command ," return ", p)
    else:
        print(command, " return ", p)
        exit(p)
