import hashlib
import json
from os import path


class BlobObject:
    DELIMITER = b"\x00"
    type = "blob"

    def __init__(self, data: bytes, path: str, oid=None, hash=hashlib.sha1):
        self.obj = BlobObject.type.encode() + BlobObject.DELIMITER + data
        self.oid = oid or hash(self.obj).hexdigest()
        self.db_path = path

    def __eq__(self, object) -> bool:
        return isinstance(self, object) and self.oid == object.oid

    def __str__(self) -> str:
        type, data = self.obj.split(self.DELIMITER)

        return json.dumps(
            {
                "oid": self.oid,
                "type": type.decode(encoding="utf-8", errors="strict"),
                "data": data.decode(encoding="utf-8", errors="strict"),
            }
        )

    def getPath(self):
        return path

    def deserialize(self) -> str:
        with open(f"{self.db_path}/{self.oid}", "wb") as out:
            out.write(self.obj)
        return self.oid
