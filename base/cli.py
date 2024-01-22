import argparse

from base.controllers.dataController import DataController


def main():
    parser = CLIParser()
    args = parser.parse_args()
    args.func(args)


class CLIParser:
    def __init__(self):
        self.dataController = DataController()

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description="A git clone cli tool for learning purposes"
        )
        commands = parser.add_subparsers(dest="command")
        commands.required = True

        # adding parser for each git command within our subparsers
        # init command
        init_p = commands.add_parser(
            "init",
            description="Initializes an empty git repository at the specified location.",
        )
        init_p.set_defaults(func=self.init)

        # object hash command
        hash_object_parser = commands.add_parser("save")
        hash_object_parser.set_defaults(func=self.save)
        hash_object_parser.add_argument("file")

        # object load command
        hash_object_parser = commands.add_parser("cat-object")
        hash_object_parser.set_defaults(func=self.cat_object)
        hash_object_parser.add_argument("oid")

        return parser.parse_args()

    # TODO: use command pattern with strategy instead of hardcoding specific commands
    # TODO: error handle when repo already initialized
    def init(self, args):
        self.dataController.init()

    # TODO: error handle when repo is not initialized
    def save(self, args):
        with open(args.file, "rb") as f:
            self.dataController.save(f.read())

    def cat_object(self, args):
        self.dataController.load(args.oid)
