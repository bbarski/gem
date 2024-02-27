import proc
from dct import dct

MENU_INPUT_STRING = 'Select option: '
NOT_IMPL = 'not implemented'
MSG = '======== GEM  ========'

with (open('input.json') as input_json):
    dct = dct(input_json)


def main_menu():
    for i in range(len(dct.posn)):
        while True:
            print(MSG)
            main_menu_label()
            what_do = int(input(MENU_INPUT_STRING))
            match what_do:
                case i:
                    proc.exe(dct.posn[i]["cmd"])


def main_menu_label():
    for i in range(len(dct.posn)):
        print(i, dct.posn[i]["cmd_desc"], dct.posn[i]["name"])
