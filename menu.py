import menu_functions

def main_menu:

    whatdo = input("What you wanna do ?")

    match whatdo:
        case "0":
            exit()
        case _:
            print("no no")
