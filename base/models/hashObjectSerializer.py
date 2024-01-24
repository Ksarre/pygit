from base.models.blobObject import BlobObject


class HashObjectSerializer:
    DELIMITER = b"\x00"
    BLOB = "blob"

    def __init__(self, db_path: str):
        self.db_path = db_path
        return

    def serialize(self, oid: str, type=BLOB) -> BlobObject:
        if type == "blob":
            return self._serializeBlob(oid, self.db_path)
        else:
            raise TypeError(f"Unsupported type: {type}")

    def _serializeBlob(self, oid: str, db_path: str):
        with open(f"{db_path}/{oid}", "rb") as f:
            obj = f.read()
        type, data = obj.split(HashObjectSerializer.DELIMITER)
        type = type.decode()

        if HashObjectSerializer.BLOB != type:
            raise TypeError(f"Expected type {HashObjectSerializer.BLOB} but got {type}")
        return BlobObject(data, db_path, oid)
