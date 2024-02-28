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
            main_menu_label()
            try:
                what_do = int(input(MENU_INPUT_STRING))
            except ValueError:
                proc.cls()
            else:
                match what_do:
                    case i:
                        for j in range(len(dct.posn[i]["cmd"])):
                            proc.exe(dct.posn[i]["cmd"][j])


def main_menu_label():
    print(MSG)
    for i in range(len(dct.posn)):
        print(i, dct.posn[i]["cmd_desc"], dct.posn[i]["name"])
