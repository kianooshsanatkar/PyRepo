from unittest import TestCase
from unittest.mock import Mock
from repo.core.baserpo import BaseRepository

class BaseRepositoryTest(TestCase):

    def test_get(self):
        ctx = Mock()
        repo = BaseRepository(ctx)

        with self.assertRaises(NotImplementedError):
            repo.get('some id')
 
    def test_add(self):
        ctx = Mock()
        ctx.add = Mock()
        repo = BaseRepository(ctx)
        obj = Mock()
        repo.add(obj)
        ctx.add.assert_called_once_with(obj)

    def test_remove(self):

        ctx = Mock()
        ctx.remove = Mock()
        repo = BaseRepository(ctx)
        obj = Mock()
        repo.remove(obj)
        ctx.remove.assert_called_once_with(obj)