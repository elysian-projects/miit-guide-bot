from typing import List

from ..constants.state import *
from ..types.location import Point
from ..utils.location import (format_location_for_database, format_point_data,
                              is_valid_location)


class StateManager:
    __location: str | None
    __current_step: int
    __max_steps: int
    __points_list: List[Point]

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


    def set_points_list(self, points_list: List[object]) -> None:
        self.__points_list = [format_point_data(_point) for _point in points_list]
        self.__max_steps = len(points_list)


    def next_step(self) -> None:
        self.__current_step += 1

        if(self.__current_step == self.__max_steps - 1):
            self.is_end = True


    def get_location(self) -> str:
        return self.__location

    def get_current_step(self) -> int:
        return self.__current_step

    def get_max_steps(self) -> int:
        return self.__max_steps

    def get_points_list(self) -> List[Point]:
        return self.__points_list


    def get_point_data(self) -> Point:
        data = self.__points_list
        step = self.__current_step

        if(len(data) == 0 or step >= len(data)):
            return Point(None, None, None, [])

        return data[step]


    def is_location_chosen(self) -> bool:
        return self.__location != None


    def reset_data(self) -> None:
        self.__location = DEFAULT_LOCATION
        self.__current_step = DEFAULT_CURRENT_STEP
        self.__max_steps = DEFAULT_MAX_STEPS
        self.__points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END
