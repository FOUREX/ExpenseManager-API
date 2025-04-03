from didiator import Mediator

from src.application.test.commands.create_test import CreateTest, CreateTestHandler


def setup_test_handlers(mediator: Mediator):
    mediator.register_command_handler(CreateTest, CreateTestHandler)
