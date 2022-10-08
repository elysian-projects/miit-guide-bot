from .external import Enumerable, unique


@unique
class Location(Enumerable):
    UNKNOWN = "unknown"
    STREET = "Улица"
    BUILDING_1 = "Корпус 1"
