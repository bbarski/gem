import cmd
import inputs as inp
from db import Db as db

MENU_INPUT_STRING = 'Select option: '
NOT_IMPL = 'not implemented'
MSG = '======== GEM installer ========'

with open('apps.json') as apps_json:
    db = db(apps_json)


def main_menu():
    while True:
        print(MSG)
        draw_main_menu()
        what_do = input(MENU_INPUT_STRING)
        match what_do:
            case "0":
                exit()
            case "1":
                install_sub_menu()
            case "3":
                print(NOT_IMPL)
            case _:
                cmd.cls()


def install_sub_menu():
    for i in range(len(db.apps)):
        while True:
            print(MSG)
            inst_sub_menu_label()
            what_do = int(input(MENU_INPUT_STRING))
            match what_do:
                case i:
                    cmd.do(db.apps[i]["instl_cmds"])


def inst_sub_menu_label():
    for i in range(len(db.apps)):
        print(i, ")", "install ", db.apps[i]["name"])


def draw_main_menu():
    menu = """
    0) Exit
    1) Go to install games sub menu
    2) Go to download games data sub menu
    3) Go to run games sub menu
    """
    print(menu)

