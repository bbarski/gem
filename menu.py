import cmd
import inputs as inp
from apps import Apps as apps

with open('apps.json') as appsjson:
    apps=apps(appsjson)

def main_menu():

    while True:
        for i in range(len(apps.app)):
            print("App #",i,"=>",apps.app[i]['name'])

        title()
    
        draw_main_menu()

        whatdo = input("Select option: ")

        match whatdo:
            case "0":
                exit()
            case "1":
                install_sub_menu()
            case "2":
                games_dat_sub_menu()
            case "3":
                print("not impleinpnted")
            case _:
                cmd.cls()

def install_sub_menu():

    while True:
        
        title()

        draw_inst_sub_menu()

        whatdo = input("Select option: ")

        match whatdo:
            case "A":
               cmd.do(inp.ADD_TW_GMS_REP)
               cmd.do(inp.ADD_TW_GMS_TLS_REP)
               cmd.do(inp.ACCPT_REP_GPGKEYS)
            case "B":
               main_menu() 
            case "E":
                exit()
            case "0":
               cmd.do(apps.app[0]['instl_cmds'])
            case "1":
               cmd.do(apps.instl_cmds)
               cmd.do(inp.GETDOOM3DEMO)
               cmd.do(inp.EXTRDOOM3PAKS)
               cmd.do(inp.MKDIRDHEWM3)
               cmd.do(inp.CPDOOM3DEMODAT)
            case "2":
               cmd.do(inp.QUAKESPASMINSTLL)
            case "3":
               cmd.do(inp.DSDADOOM)
            case "4":
               cmd.do(inp.DUNELEGACY)
            case "5":
               cmd.do(inp.FHEROES2)
            case "6":
               cmd.do(inp.OPENTYRIAN)
            case "7":
               cmd.do(inp.XRICK)
            case "8":
               cmd.do(inp.OPENXCOM)
            case "9":
               cmd.do(inp.SCUMMVM)
            case "10":
               cmd.do(inp.REMINISCENCE)
            case _:
               cmd.cls()


def games_dat_sub_menu():

    while True:
        
        title()

        draw_games_dat_sub_menu()

        whatdo = input("Select option: ")

        match whatdo:
            case "B":
               main_menu() 
            case "0":
                exit()
            case "1":
                cmd.do(inp.GETDOOM3DEMO)
                cmd.do(inp.EXTRDOOM3PAKS)
                cmd.do(inp.MVDOOM3DEMODAT)

def title():
    print("======== GEM installer ========")

def draw_main_menu():
    menu = """
    0) Exit
    1) Go to install games sub menu
    2) Go to download games data sub menu
    3) Go to run games sub menu
    """
    print(menu)

def draw_inst_sub_menu():
    menu = """
    A) Add SUSE TW games repos
    B) Back to main menu
    E) Exit
    0) install lgogdownloader - linux gog data downloader
    1) install dhewm3 - doom3 linux port
    2) install quakespasm - quake1 linux port
    3) install dsda-doom - DOOM 1 linux port
    4) install dunelegacy - DUNE 2 linux port
    5) install fheroes2 - HOMM2 linux port
    6) install opentyrian - Tyrian 2000 linux port
    7) install xrick - Rick Dangerous linux port
    8) install openxcom
       UFO: Enemy Unknown / X-COM: UFO Defense linux port
    9) install scummvm - rpg gainps runer
    10) install REminiscence - Flashback linux port
    """
    print(menu)

    
def draw_games_dat_sub_menu():
    menu = """
    B) Back to main menu
    0) Exit
    1) get Doom 3 demo game data
    """
    print(menu)

