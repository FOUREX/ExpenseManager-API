from didiator import Mediator

from src.application.expense.queries.get_by_id import GetByID, GetByIDHandler
from src.application.expense.queries.get_between import GetBetween, GetBetweenHandler

from src.application.expense.commands.create_expense import CreateExpense, CreateExpenseHandler
from src.application.expense.commands.edit_expense import EditExpense, EditExpenseHandler
from src.application.expense.commands.delete_expense import DeleteExpense, DeleteExpenseHandler


def setup_expense_handlers(mediator: Mediator):
    mediator.register_query_handler(GetByID, GetByIDHandler)
    mediator.register_query_handler(GetBetween, GetBetweenHandler)

    mediator.register_command_handler(CreateExpense, CreateExpenseHandler)
    mediator.register_command_handler(EditExpense, EditExpenseHandler)
    mediator.register_command_handler(DeleteExpense, DeleteExpenseHandler)
