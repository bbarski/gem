import os
import subprocess

def cls():
    print("\033[H\033[J", end="")

def suse_install(command) :
    
    p = subprocess.Popen(command)
    p.wait()
    
def mint_install(pkgName) :
    command = ['sudo',
               'apt-get',
               '-yq',
               'install',
               pkgName]
    
    p = subprocess.Popen(command)
    p.wait()
