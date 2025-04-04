from didiator import Mediator, MediatorImpl, CommandDispatcherImpl, QueryDispatcherImpl, EventObserverImpl
from didiator.middlewares.di import DiMiddleware, DiScopes
from didiator.interface.utils.di_builder import DiBuilder

from src.infrastructure.di.constants import DiScope
from src.infrastructure.mediator.handlers.expense import setup_expense_handlers


def get_mediator() -> Mediator:
    raise NotImplementedError


def init_mediator(di_builder: DiBuilder) -> Mediator:
    middlewares = (
        DiMiddleware(di_builder, scopes=DiScopes(DiScope.REQUEST)),
    )

    command_dispatcher = CommandDispatcherImpl(middlewares=middlewares)
    query_dispatcher = QueryDispatcherImpl(middlewares=middlewares)
    event_observer = EventObserverImpl(middlewares=middlewares)

    mediator = MediatorImpl(command_dispatcher, query_dispatcher, event_observer)

    return mediator


def setup_mediator(mediator: Mediator):
    setup_expense_handlers(mediator)
