from typing import Any


class StateManager:
    __state: Any

    def __init__(self, initial_state: Any):
        self.__state = initial_state

    def get_state(self) -> Any:
        return self.__state

    def set_state(self, updated_value: Any) -> None:
        self.__state = updated_value
