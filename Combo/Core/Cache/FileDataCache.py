from Combo.Core.Cache.DataCache import DataCache
import os
import pickle


class FileDataCache(DataCache):
    """
    store data in the filesystem.
    """
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if not os.path.exists(self.path):
            raise Exception

    def exist(self, type_id: str, cache_id: str):
        if os.path.exists(os.path.join(self.path, type_id, cache_id)):
            return True
        else:
            return False

    def add(self, type_id: str, cache_id: str, data):
        if os.path.exists(os.path.join(self.path, type_id, cache_id)):
            return True

        if not os.path.exists(os.path.join(self.path, type_id)):
            os.mkdir(os.path.join(self.path, type_id))
        if not os.path.exists(os.path.join(self.path, type_id)):
            return False

        with open(os.path.join(self.path, type_id, cache_id), 'wb') as f:
            pickle.dump(data, f)
        return True

    def update(self, type_id: str, cache_id: str, data):
        if not os.path.exists(os.path.join(self.path, type_id)):
            os.mkdir(os.path.join(self.path, type_id))
        if not os.path.exists(os.path.join(self.path, type_id)):
            return False

        with open(os.path.join(self.path, type_id, cache_id), 'wb') as f:
            pickle.dump(data, f)
        return True

    def fetch(self, type_id: str, cache_id: str):
        if not os.path.exists(os.path.join(self.path, type_id, cache_id)):
            return None

        data = None
        with open(os.path.join(self.path, type_id, cache_id), 'rb') as f:
            data = pickle.load(f)
        return data
