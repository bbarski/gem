import menu_functions
import menu_entries as me

def main_menu():
    
    while True:

        title()
    
        draw_main_menu()

        whatdo = input("Select option: ")

        match whatdo:
            case "0":
                exit()
            case "1":
               install_sub_menu()
            case "2":
               menu_functions.command(me.DHEWM3)
            case "3":
               menu_functions.command(me.QUAKESPASM)
            case _:
               menu_functions.cls()

def install_sub_menu():

    while True:
        
        title()

        draw_inst_sub_menu()

        whatdo = input("Select option: ")

        match whatdo:
            case "B":
               main_menu() 
            case "0":
                exit()
            case "1":
               menu_functions.command(me.STEAMCMD)
            case "2":
               menu_functions.command(me.DHEWM3)
            case "3":
               menu_functions.command(me.QUAKESPASM)
            case "4":
               menu_functions.command(me.DSDADOOM)
            case "5":
               menu_functions.command(me.DUNELEGACY)
            case "6":
               menu_functions.command(me.ADD_FHEROES2_REP) 
               menu_functions.command(me.FHEROES2)
            case "7":
               menu_functions.command(me.OPENTYRIAN)
            case "8":
               menu_functions.command(me.XRICK)
            case "9":
               menu_functions.command(me.OPENXCOM)
            case "10":
               menu_functions.command(me.SCUMMVM)
            case "11":
               menu_functions.command(me.REMINISCENCE)
            case _:
               menu_functions.cls()

def title():
    print("======== GEM installer ========")

def draw_main_menu():
    menu = """
    0) Exit
    1) Go to install sub menu
    2) Go to download game data sub menu
    3) Go to run game sub menu
    """
    print(menu)

def draw_inst_sub_menu():
    menu = """
    B) Back to main menu
    0) Exit
    1) install steamcmd - linux steam data downloader
    2) install dhewm3 - doom3 linux port
    3) install quakespasm - quake1 linux port
    4) install dsda-doom - DOOM 1 linux port
    5) install dunelegacy - DUNE 2 linux port
    6) install fheroes2 - HOMM2 linux port
    7) install opentyrian - Tyrian 2000 linux port
    8) install xrick - Rick Dangerous linux port
    9) install openxcom
       UFO: Enemy Unknown / X-COM: UFO Defense linux port
    10) install scummvm - rpg games runer
    11) install REminiscence - Flashback linux port
    """
    print(menu)
