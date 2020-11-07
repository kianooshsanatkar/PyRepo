class UnitOfWork:

    def __init__(self, _contxt, factory_dict: dict, auto_commit = False):
        pass

    def get_repository(self, repo):
        pass

    def commit(self):
        pass

    def close(self):
        pass

    def connect(self):
        pass

    def __enter__(self, *args):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __repr__(self):
        pass