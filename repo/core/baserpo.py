class BaseRepository:

    def __init__(self, context):
        self.__ctx = context

    def get(self, uid): 
        raise NotImplementedError()

    def add(self, obj):
        self.__ctx.add(obj)

    def remove(self, obj):
        self.__ctx.remove(obj)