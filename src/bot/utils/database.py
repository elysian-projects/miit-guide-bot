import json
from typing import List

from ..types.database import Location


class Database:
    __data: str

    def __init__(self):
        with open("./static/data.json", "r") as file:
            self.__data = file.read()

    def connect(self) -> None:
        pass

    def get_location(self, location: str) -> List[Location] | None:
        try:
            data = self.parse_response(self.__data)["locations"]

            return data["locations"]

        except Exception as e:
            # print(repr(e))
            return None

    def parse_response(self, response: str):
        return json.loads(response)
