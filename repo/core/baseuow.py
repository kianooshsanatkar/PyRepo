class UnitOfWork:

    def __init__(self, _contxt, factory_dict: dict, auto_commit = False):
        super().__init__()
        self.__ctx = _contxt
        self.__factory = factory_dict
        self.pool = {}

    def get_repository(self, repo):
        """
        get repository, eighter from pool if already built or eighther build a new one

        Args:
            repo ([type]): repository name to get it eigher from pool or eigher build it

        Raises:
            KeyError: [description]

        Returns:
            [type]: [description]
        """
        r = self.pool.get(repo)
        if not r:
            _ = self.__factory.get(repo)
            r = _(self.__ctx)
            self.pool[repo] = r
        if not r:
            raise KeyError("Repository does not exist!")
        return r

    def commit(self):
        self.__ctx.commit()

    def close(self):
        self.__ctx.close()

    def connect(self):
        self.__ctx.connect()

    def __enter__(self, *args):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.__ctx) + ")"