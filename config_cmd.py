import glob
import proc
import strings
import json


def find_files(fpattern):
    return glob.glob(fpattern)


def display_files(files):
    if files:
        print("Founded config files")
        for i in range(len(files)):
            print(i, ")", files[i])
    if not files:
        print("No config files found")


def select_file(files):
    try:
        opt = int(input(strings.SLCT_OPT))
    except ValueError:
        proc.cls()
    else:
        for i in range(len(files)):
            match opt:
                case i:
                    return files[i]


def open_config(fname):
    return json.load(open(fname))


def init_config():
    fpattern = "configJSONS/*.json"
    files = find_files(fpattern)
    display_files(files)
    return open_config(select_file(files))
