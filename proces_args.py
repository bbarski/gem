import argparse
import menu


class ProcessArgs:
    def get_args(argv=None):
        parser = argparse.ArgumentParser(description='create menu from json of commands')
        parser.add_argument(
            '--j',
            '--json',
            required=True,
            type=argparse.FileType('r'),
            help='path to config json',
            action=menu.main_menu(json.load(args.json)),
        )
        return parser.parse_args()
