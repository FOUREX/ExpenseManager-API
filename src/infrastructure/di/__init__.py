from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import AsyncExecutor

from didiator.utils.di_builder import DiBuilderImpl
from didiator.interface.utils.di_builder import DiBuilder

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, AsyncEngine

from src.infrastructure.di.constants import DiScope
from src.infrastructure.config import DBConfig
from src.infrastructure.db import build_sa_engine, build_async_session_maker, get_async_session
from src.infrastructure.db.uow import build_uow
from src.application.common.interfaces.uow import UnitOfWork


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = [DiScope.APP, DiScope.REQUEST]
    di_builder = DiBuilderImpl(
        di_container=di_container,
        di_executor=di_executor,
        di_scopes=di_scopes
    )

    return di_builder


def setup_di_builder(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(lambda *_: di_builder, scope=DiScope.APP), DiBuilder))

    setup_config_factories(di_builder)
    setup_db_factories(di_builder)


def setup_config_factories(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(lambda *_: DBConfig(), scope=DiScope.APP), DBConfig))


def setup_db_factories(di_builder: DiBuilder):
    di_builder.bind(bind_by_type(Dependent(build_sa_engine, scope=DiScope.APP), AsyncEngine, covariant=True))
    di_builder.bind(
        bind_by_type(
            Dependent(build_async_session_maker, scope=DiScope.APP),
            async_sessionmaker[AsyncSession]
        )
    )
    di_builder.bind(bind_by_type(Dependent(get_async_session, scope=DiScope.REQUEST), AsyncSession, covariant=True))

    di_builder.bind(bind_by_type(Dependent(build_uow, scope=DiScope.REQUEST), UnitOfWork))
