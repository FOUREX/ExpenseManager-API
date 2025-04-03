from src.application.common.exceptions.base import ServerError


class CommitError(ServerError):
    pass


class RollbackError(ServerError):
    pass
