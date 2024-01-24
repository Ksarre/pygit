import os
import sys

from base.models.blobObject import BlobObject
from base.data.hashObjectSerializer import HashObjectSerializer

GET_DIR = ".pygit"
OBJECT_DB_PATH = f"{GET_DIR}/objects"


class DataController:
    def __init__(self):
        self.INIT_DIR = ".pygit"
        self.obj_serializer = HashObjectSerializer(OBJECT_DB_PATH)

    def init(self):
        os.makedirs(GET_DIR)
        os.makedirs(f"{OBJECT_DB_PATH}")
        self.object_db = f"{OBJECT_DB_PATH}"

    def save(self, data: bytes) -> str:
        obj = BlobObject(data, OBJECT_DB_PATH)
        obj.deserialize()
        return obj.oid

    def load(self, oid: str, _type=None) -> BlobObject:
        obj = (
            self.obj_serializer.serialize(oid, _type)
            if _type is not None
            else self.obj_serializer.serialize(oid)
        )
        # might need a flush here if there's ordering issues
        print(obj)
        # sys.stdout.buffer.write(obj.__str__())
        return obj
