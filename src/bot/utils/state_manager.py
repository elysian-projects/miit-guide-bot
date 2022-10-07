from typing import Any

from ..types.location import Location


class StateManager:
    __location: Location
    __current_step: int
    __max_steps: int

    def __init__(self):
        self.__location = Location.UNKNOWN
        self.__current_step = 0
        self.__max_steps = 0

    def get_location(self) -> str:
        return self.__location

    def set_location(self, location: Location, max_steps: int) -> None:
        self.__location = location
        self.__max_steps = max_steps

    def next_step(self) -> None:
        self.__current_step = (self.__current_step + 1) % self.__max_steps
