from collections import namedtuple
from mongoengine import connection

from ..core.baseuow import UnitOfWork


class MongoUnitOfWork(UnitOfWork):

    def __init__(self, db=None, alias=None, host=None, port=None, auto_commit=False):
        Context = namedtuple('Context', ['db', 'alias', 'host', 'port'])
        super().__init__(Context(db, alias, host, port), auto_commit)

    def connect(self):
        connection.connect(self.__ctx__.db)

    def close(self):
        connection.disconnect(self.__ctx__.db)

    # todo: currently mongoEngine doesn't fully supported transactions in mongodb so commit is empty but remain to
    #  preserve the architecture, we shall not be depend to the orm but the orm must depend to the model. so I decided
    #  to adapt orm, and wait for mongoEngine to support transactions.
    def commit(self):
        pass
