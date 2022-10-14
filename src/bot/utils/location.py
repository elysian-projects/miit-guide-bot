from ..constants.locations import AVAILABLE_LOCATIONS
from ..types.location import Location


def get_location_label(location: str) -> str | None:
    for _, _location in Location.items():
        if(location.strip() == _location["label"] or location.strip() == _location["value"]):
            return _location["label"]
    return None


def get_location_value(location: str) -> str | None:
    for _, _location in Location.items():
        if(location.strip() == _location["label"] or location.strip() == _location["value"]):
            return _location["value"]
    return None


def is_valid_location(location: str) -> bool:
    return location.strip() in [_location["value"] for _location in AVAILABLE_LOCATIONS] \
        or location.strip() in [_location["label"] for _location in AVAILABLE_LOCATIONS]


def format_location_for_database(location: str) -> str | None:
    return get_location_value(location)
