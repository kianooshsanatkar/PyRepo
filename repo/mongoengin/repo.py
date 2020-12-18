from ..core.baserpo import BaseRepository


class MongoEngineRepository(BaseRepository):

    def __init__(self, context):
        super().__init__(context)

    def get(self, model, uid):
        return model.get(id=uid)

    def add(self, obj):
        return obj.save()

    def remove(self, obj):
        return obj.remove()
