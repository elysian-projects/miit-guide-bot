from ..constants.locations import AVAILABLE_LOCATIONS
from ..types.location import Location


def is_valid_location(location: str) -> bool:
    return location in [_location["value"] for _location in AVAILABLE_LOCATIONS] \
        or location in [_location["label"] for _location in AVAILABLE_LOCATIONS]


def format_location_for_database(location: str) -> str | None:
    for _, _location in Location.items():
        if(location == _location["label"] or location == _location["value"]):
            return _location["value"]

    return None
