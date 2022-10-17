from typing import Any

from ..constants.locations import Location
from ..constants.state import *
from ..types.state import StateField
from ..utils.location import (format_location_for_database, get_location_value,
                              is_valid_location)


class StateManager:
    __location: str | None
    __current_step: int
    __max_steps: int
    __points_list: list[list[object]]

    is_end: bool

    def __init__(self):
        self.__location = DEFAULT_LOCATION
        self.__current_step = DEFAULT_CURRENT_STEP
        self.__max_steps = DEFAULT_MAX_STEPS
        self.__points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END


    def set_location(self, location: str) -> None:
        if(not is_valid_location(location)):
            raise TypeError("Incorrect location was given!")

        self.__location = format_location_for_database(location)
        self.__max_steps = len(Location[get_location_value(location)])


    def set_points_list(self, points_list: list[Any]) -> None:
        self.__points_list = points_list
        self.__max_steps = len(points_list)


    def next_step(self) -> None:
        self.__current_step += 1

        if(self.get(StateField.CURRENT_STEP) == self.get(StateField.MAX_STEPS) - 1):
            self.is_end = True


    def get(self, field: StateField) -> str | None:
        current_state = {
            StateField.LOCATION: self.__location,
            StateField.CURRENT_STEP: self.__current_step,
            StateField.MAX_STEPS: self.__max_steps,
            StateField.POINTS_LIST: self.__points_list,
            StateField.IS_END: self.is_end
        }

        if(field in current_state):
            return current_state[field]

        return None


    def get_current_step_data(self, field: str) -> str | None:
        data = self.get(StateField.POINTS_LIST)
        step = self.get(StateField.CURRENT_STEP)

        if(len(data) == 0 or step >= len(data) or not field in data[step]):
            return None

        return data[step][field]


    def is_location_chosen(self) -> bool:
        return self.get(StateField.LOCATION) != None


    def reset_data(self) -> None:
        self.__location = DEFAULT_LOCATION
        self.__current_step = DEFAULT_CURRENT_STEP
        self.__max_steps = DEFAULT_MAX_STEPS
        self.__points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END
