from typing import List

from ..utils.database import parse_response


class Database:
    __data: str

    def __init__(self):
        with open("./static/data.json", "r", encoding = 'UTF-8') as file:
            self.__data = file.read()

    def connect(self) -> None:
        pass

    def get_location(self, location: str) -> List[object] | None:
        data = parse_response(self.__data)

        for _location in data["locations"]:
            if(location == _location):
                return data["locations"][_location]

        return None
