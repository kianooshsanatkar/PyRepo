from uuid import uuid4

from repo import MongoEngineRepository, MongoUnitOfWork

from example.mongoexample.models import User


def main():
    with MongoUnitOfWork('Mongo_Test', None, 'localhost', None) as uow:
        joe = User(uid=uuid4(), username='Joe', email='Asghar@yahoo.com', password='Pa$$word')
        repo = uow.get_repository('MongoEngineRepository')
        repo.add(joe)
        uow.commit()


if __name__ == '__main__':
    MongoUnitOfWork.add_repository('MongoEngineRepository', MongoEngineRepository)
    main()
