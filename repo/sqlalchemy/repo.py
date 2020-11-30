from ..core.baserpo import BaseRepository


class SqlAlchemyRepository(BaseRepository):

    def get(self, model: type, query):
        return self.__ctx__.query(model).get(query)