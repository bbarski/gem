import os
import subprocess

def cls():
    print("\033[H\033[J", end="")

def do(command) :
    
    p = subprocess.Popen(command)
    p.wait()
    
