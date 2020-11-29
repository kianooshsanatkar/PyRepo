from unittest import TestCase, main as unittest_main
from unittest.mock import Mock
from repo.core.baseuow import UnitOfWork
from uuid import uuid4


class UnitOfWorkTest(TestCase):

    def test_enter(self):
        ctx = Mock()
        ctx.connect = Mock()

        with UnitOfWork(ctx, {}) as uow:
            pass
        ctx.connect.assert_called_once()

    def test_exit(self):
        ctx = Mock()
        ctx.close = Mock()

        with UnitOfWork(ctx, {}) as uow:
            pass

        ctx.close.assert_called_once()

    def test_commit(self):
        ctx = Mock()
        ctx.commit = Mock()

        with UnitOfWork(ctx, {}) as uow:
            uow.commit()
        ctx.commit.assert_called_once()

    def test_connect(self):
        ctx = Mock()
        ctx.connect = Mock()

        with UnitOfWork(ctx, {}) as uow:
            uow.close()
            uow.connect()

        self.assertEqual(2, ctx.connect.call_count)

    def test_repo_call(self):
        ctx = Mock()
        repo = Mock(return_value=uuid4())
        __repo_factory = {repo.__class__.__name__: repo}
        UnitOfWork.add_repositories(__repo_factory)
        with UnitOfWork(ctx) as uow:
            r = uow.get_repository(repo.__class__.__name__)
            r2 = uow.get_repository(repo.__class__.__name__)
            self.assertEqual(r, r2)

        repo.assert_called_once()
