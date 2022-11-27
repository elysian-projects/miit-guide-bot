from typing import List

from ..types.location import Location

Locations = {
    "street": Location("Улица", "street"),
    "building_1": Location("Корпус 1", "building_1")
}

AVAILABLE_LOCATIONS: List[Location] = [Locations[location] for location in Locations]

LOCATION_LABELS = [_location.label for _location in AVAILABLE_LOCATIONS]
LOCATION_VALUES = [_location.value for _location in AVAILABLE_LOCATIONS]