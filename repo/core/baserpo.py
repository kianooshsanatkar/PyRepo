class BaseRepository:

    def __init__(self, context):
        self.__ctx__ = context

    def get(self, uid): 
        raise NotImplementedError()

    def add(self, obj):
        self.__ctx__.add(obj)

    def remove(self, obj):
        self.__ctx__.remove(obj)