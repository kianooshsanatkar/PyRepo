class UnitOfWork:

    __repo = {}

    @staticmethod
    def add_repositories(repositories: dict):
        """Add one or more repositories as dictionary

        Args:

            repose (dict): repositories as dictionary. e.g. {'repository_class_name': RepositoryClass, ...}
        """
        UnitOfWork.__repo.update(repositories)

    def __init__(self, _context, auto_commit=False):
        super().__init__()
        self.__ctx = _context
        self.pool = {}

    def get_repository(self, repo: str):
        """get repository, either from pool if already built or eighther build a new one.
        Any new repository will be added to the pool and in the next call will be retrieved from the pool.

        Args:

            repo (str): 'insert repository name to get it either from pool or either a new one'

        Raises:

            KeyError: 'Inserted Repository Name does not exist'

        Returns:

            Repository: [description]
        """
        r = self.pool.get(repo)
        if not r:
            _ = self.__repo.get(repo)
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
