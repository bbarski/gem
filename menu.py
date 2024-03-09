import proc
from jdct import jdct

MENU_INPUT_STRING = 'Select option: '

with (open('input.json') as json_strm):
    jdct = jdct(json_strm)


def main_menu():
    for i in range(len(jdct.posn)):
        while True:
            main_menu_label()
            try:
                what_do = int(input(MENU_INPUT_STRING))
            except ValueError:
                proc.cls()
            else:
                match what_do:
                    case i:
                        for j in range(len(jdct.posn[i]["cmd"])):
                            proc.exe(jdct.posn[i]["cmd"][j])


def main_menu_label():
    print(jdct.json_name)
    for i in range(len(jdct.posn)):
        print(i, jdct.posn[i]["cmd_desc"], jdct.posn[i]["dscrp"])