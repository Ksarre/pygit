import hashlib
import json
from os import path


class HashObject:
    HASH_DEFAULT = hashlib.sha1

    def __init__(self, data: any, path: str, oid=None, hash=HASH_DEFAULT):
        self.oid = oid or hash(data).hexdigest()
        self.data = data
        self.db_path = path

    def __eq__(self, object) -> bool:
        return isinstance(self, object) and self.oid == object.oid

    def __str__(self) -> str:
        return json.dumps(
            {
                "oid": self.oid,
                "raw": self.data.decode(encoding="utf-8", errors="strict"),
            }
        )

    def getPath(self):
        return path

    def write(self) -> str:
        with open(f"{self.db_path}/{self.oid}", "wb") as out:
            out.write(self.data)
        return self.oid

    @staticmethod
    def read(oid: str, db_path: str):
        with open(f"{db_path}/{oid}", "rb") as f:
            return HashObject(f.read(), db_path, oid)
