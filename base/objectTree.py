import os


class ObjectTree:
    def __init__(self):
        return

    # depth first traversal
    # TODO: need to mimic .gitignore behavior
    @staticmethod
    def write_tree(directory="."):
        with os.scandir(directory) as it:
            for entry in it:
                full = f"{directory}/{entry.name}"

                # easy method to skip our py environment and obj db directory for now
                if ObjectTree.is_ignored(full):
                    continue

                if entry.is_file(follow_symlinks=False):
                    # TODO write the file to object store
                    print(full)
                elif entry.is_dir(follow_symlinks=False):
                    ObjectTree.write_tree(full)

    @staticmethod
    def is_ignored(path):
        return any(x in path.split("/") for x in [".pygit", ".venv"])
