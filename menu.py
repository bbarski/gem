import proc
import strings
import config_cmd

config = config_cmd.init_config()


def main_menu():
    for i in range(len(config['posn'])):
        while True:
            display_menu()
            try:
                opt = int(input(strings.SLCT_OPT))
            except ValueError:
                proc.cls()
            else:
                match opt:
                    case i:
                        for j in range(len(config['posn'][i]["cmd"])):
                            proc.exe(config['posn'][i]["cmd"][j])


def display_menu():
    print(config['json_name'])
    for i in range(len(config['posn'])):
        print(i, config['posn'][i]["cmd_desc"], config['posn'][i]["dscrp"])
