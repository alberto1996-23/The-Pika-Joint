from backend.src.command.command import Command

class OrderController:
    def __init__(self):
        self.__command: Command | None = None

    def set_command(self, command: Command) -> None:
        self.__command = command

    def run_command(self) -> None:
        if self.__command is not None:
            self.__command.execute()