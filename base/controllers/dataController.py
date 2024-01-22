import os
import sys

from base.models.hashObject import HashObject

GET_DIR = ".pygit"
OBJECT_DB_PATH = f"{GET_DIR}/objects"


class DataController:
    def __init__(self):
        self.INIT_DIR = ".pygit"

    def init(self):
        os.makedirs(GET_DIR)
        os.makedirs(f"{OBJECT_DB_PATH}")
        self.object_db = f"{OBJECT_DB_PATH}"

    def save(self, data) -> str:
        obj = HashObject(data, OBJECT_DB_PATH)
        obj.write()
        return obj.oid

    def load(self, oid) -> HashObject:
        obj = HashObject.read(oid, OBJECT_DB_PATH)
        # might need a flush here if there's ordering issues
        print(obj)
        # sys.stdout.buffer.write(obj.__str__())
        return obj
