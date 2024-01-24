from base.models.blobObject import BlobObject


class AnotherObject(BlobObject):
    def __init__(self, data: any, path: str, oid=None, hash=...):
        super().__init__(data, path, oid, hash)
