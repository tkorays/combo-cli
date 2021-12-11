import abc


class DataCache(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def exist(self, type_id: str, cache_id: str):
        """
        To check whether the data has been cached.

        :param type_id: the data type id, the same type data has the same structure.
        :param cache_id: data id identified by some fields.
        :return True if the data has been cached.
        """
        pass

    @abc.abstractmethod
    def add(self, type_id: str, cache_id: str, data):
        """
        add a new data.

        :param type_id: the data type id, the same type data has the same structure.
        :param cache_id: data id identified by some fields.
        :param data: data.
        :return True if the data has been added.
        """
        pass

    @abc.abstractmethod
    def update(self, type_id: str, cache_id: str, data):
        """
        update data.

        :param type_id: the data type id, the same type data has the same structure.
        :param cache_id: data id identified by some fields.
        :param data: data.
        :return True if the data has been updated.
        """
        pass

    @abc.abstractmethod
    def fetch(self, type_id: str, cache_id: str):
        """
        fetch data.

        :param type_id: the data type id, the same type data has the same structure.
        :param cache_id: data id identified by some fields.
        :return data.
        """
        pass
