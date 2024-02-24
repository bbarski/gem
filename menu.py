import menu_functions
import menu_entries as me

def main_menu():
    while True:
    
        draw_menu()

        whatdo = input("What you wanna do ? ")

        match whatdo:
            case "0":
                exit()
            case "1":
               menu_functions.install(me.STEAMCMD)
            case "2":
               menu_functions.install(me.DHEWM3)
            case "3":
               menu_functions.install(me.QUAKESPASM)
            case "4":
               menu_functions.install(me.DSDADOOM)
            case "5":
               menu_functions.install(me.DUNELEGACY)
            case "6":  
               menu_functions.install(me.FHEROES2)
            case "7":
               menu_functions.install(me.OPENTYRIAN)
            case "8":
               menu_functions.install(me.XRICK)
            case "9":
               menu_functions.install(me.OPENXCOM)
            case "10":
               menu_functions.install(me.SCUMMVM)
            case "11":
               menu_functions.install(me.REMINISCENCE)
            case _:
               menu_functions.cls()    

def draw_menu():
    menu = """
    What you want to do ?
    0) - exit
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
    12) get doom 3 game data from internet archive
    13) get duke nukem3D shrwr game data from internet archive
    14) get duke nukem 3D FULL game data from internet archive
    15) get classic doom1 data from steam
    16) idk
    """
    print(menu)
