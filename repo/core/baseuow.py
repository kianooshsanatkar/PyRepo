class UnitOfWork:

    __repo__ = {}

    @staticmethod
    def add_repositories(repositories: dict):
        """Add one or more repositories as dictionary

        Args:

            :param repositories: repositories as dictionary. e.g. {'repository_class_name': RepositoryClass, ...}
        """
        if type(repositories) is not dict:
            raise ValueError('repositories must be a dictionary')
        UnitOfWork.__repo__.update(repositories)

    @staticmethod
    def add_repository(repository_name: str, repository: type):
        """Add One repository to dictionary
        
        Args:

            repository_name (str): the name of repository as a key dictionary, for repository with the same name use module name separated with dot (.)

            repository (type): repository class that needed to implement, for complex object please use factory or partial approach
            
        """
        UnitOfWork.__repo__[repository_name] = repository

    def __init__(self, _context, auto_commit=False):
        super().__init__()
        self.__ctx__ = _context
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
            _ = self.__repo__.get(repo)
            r = _(self.__ctx__)
            self.pool[repo] = r
        if not r:
            raise KeyError("Repository does not exist!")
        return r

    def commit(self):
        self.__ctx__.commit()

    def close(self):
        self.__ctx__.close()

    def connect(self):
        self.__ctx__.connect()

    def __enter__(self, *args):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.__ctx__) + ")"
