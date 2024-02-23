import menu_functions
import messeges

def menu_logic():
    while True:
       messeges.welcome_msg() 
       draw_menu() 
       whatdo = input(messeges.enter_nmbr_msg())
       match whatdo:
           case "0":
               exit()
           case "1":
               menu_functions.suse_install('steamcmd')
           case "2":
               menu_functions.suse_install('dhewm3')
           case "3":
               menu_functions.suse_install('quakespasm')
           case "4":
               menu_functions.suse_install('dsda-doom')
           case "5":
               menu_functions.suse_install('dunelegacy')
           case "6":  
               menu_functions.suse_install('fheroes2')
           case "7":
               menu_functions.suse_install('opentyrian')
           case "8":
               menu_functions.suse_install('xrick')
           case "9":
               menu_functions.suse_install('openxcom')
           case "10":
               menu_functions.suse_install('scummvm')
           case "11":
               menu_functions.suse_install('reminiscence')
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

