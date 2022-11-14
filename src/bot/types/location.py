from typing import List

from .external import Enumerable


class Location:
    label: str
    value: str

    def __init__(self, label: str, value: str):
        if(label == "" or value == ""):
            raise("Empty argument!")

        self.label = label
        self.value = value


class LocationProps(Enumerable):
    value: str = "value"
    label: str = "label"


class Point:
    name: str
    description: str
    #TODO: исправить при внедрении функционала отправления нескольких картинок в одном сообщении - `str | List[str]`
    picture: str
    links: List[str]

    def __init__(self, name: str = None, description: str = None, picture: str = None, links: List[str] = []):
        self.name = name
        self.description = description
        self.picture = picture
        self.links = links

    def __eq__(self, __o: object) -> bool:
        return self.__dict__ == __o.__dict__