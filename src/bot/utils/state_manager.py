from ..types.location import Location


class StateManager:
    __location: Location
    __current_step: int
    __steps: int

    def __init__(self):
        self.__location = Location.UNKNOWN
        self.__current_step = 0
        self.__steps = 0

    def get_location(self) -> str:
        return self.__location

    def set_location(self, location: str) -> None:
        self.__location = location
        self.__steps = self.__get_steps_amount(location = location)

    def next_step(self) -> None:
        self.__current_step = (self.__current_step + 1) % self.__steps

    def is_location_chosen(self) -> bool:
        return self.__location != Location.UNKNOWN

    def is_location_available(self, location: str) -> bool:
        return location in Location

    def reset_data(self) -> None:
        self.__location = Location.UNKNOWN
        self.__current_step = 0
        self.__steps = 0

    def __get_steps_amount(self, location: str) -> int:
        return 0
