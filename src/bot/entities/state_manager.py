from typing import Any

from ..constants.state import *
from ..types.location import Location
from ..utils.location import (format_location_for_database, get_location_value,
                              is_valid_location)


class StateManager:
    __location: str | None
    __current_step: int
    __amount_of_points: int
    __points_list: list[list[object]]

    def __init__(self):
        self.__location = DEFAULT_LOCATION
        self.__current_step = DEFAULT_CURRENT_STEP
        self.__amount_of_points = DEFAULT_AMOUNT_OF_POINTS
        self.__points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END


    def get_location(self) -> str:
        return self.__location


    def set_location(self, location: str) -> None:
        if(not is_valid_location(location)):
            raise TypeError("Incorrect location was given!")

        self.__location = format_location_for_database(location)
        self.__amount_of_points = len(Location[get_location_value(location)])


    def get_points_list(self) -> list[Any]:
        return self.__points_list


    def set_points_list(self, points_list: list[Any]) -> None:
        self.__points_list = points_list
        self.__amount_of_points = len(points_list)


    def get_current_step(self) -> int:
        return self.__current_step


    def get_data_by_field(self, field: str) -> str | None:
        try:
            data = self.get_points_list()
            step = self.get_current_step()

            if(len(data) == 0 or step >= len(data)):
                return None

            return self.get_points_list()[self.get_current_step()][field]

        except KeyError as e:
            print(repr(e))
            return None


    def next_step(self) -> None:
        self.__current_step += 1

        if(self.__current_step == (self.__amount_of_points - 1)):
            self.is_end = True


    def is_location_chosen(self) -> bool:
        return self.__location != None


    def reset_data(self) -> None:
        self.__location = DEFAULT_LOCATION
        self.__current_step = DEFAULT_CURRENT_STEP
        self.__amount_of_points = DEFAULT_AMOUNT_OF_POINTS
        self.__points_list = DEFAULT_POINTS_LIST
        self.is_end = DEFAULT_IS_END
        self.__points_list = []
