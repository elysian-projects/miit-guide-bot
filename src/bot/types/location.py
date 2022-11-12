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