from ..types.location import Location
from ..utils.location import format_location_for_database, is_valid_location


class StateManager:
    __location: str
    __current_step: int


    def __init__(self):
        self.__location = Location["unknown"]["value"]
        self.__current_step = 0


    def get_location(self) -> str:
        return self.__location


    def set_location(self, location: str) -> None:
        if(not is_valid_location(location)):
            raise TypeError("Incorrect location was given!")

        self.__location = format_location_for_database(location)


    def get_current_step(self) -> int:
        return self.__current_step


    def next_step(self) -> None:
        self.__current_step = self.__current_step + 1


    def is_location_chosen(self) -> bool:
        return self.__location != Location["unknown"]["value"]


    def reset_data(self) -> None:
        self.__location = Location["unknown"]["value"]
        self.__current_step = 0
