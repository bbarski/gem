import os
import subprocess


def cls():
    print("\033[H\033[J", end="")


def exe(command):
    p = subprocess.Popen(command,shell=True)
    p.wait()
