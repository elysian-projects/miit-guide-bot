from ..constants.locations import LOCATION_LABELS, LOCATION_VALUES, Locations
from ..types.location import LocationProps


def get_location_property(location: str, prop: LocationProps) -> str | None:
    for _, _location in Locations.items():
        if(location.strip() == _location.label or location.strip() == _location.value):
            return _location.label if prop == LocationProps.label else _location.value
    return None


def is_valid_location(location: str) -> bool:
    return location.strip() in LOCATION_VALUES \
        or location.strip() in LOCATION_LABELS


def format_location_for_database(location: str) -> str | None:
    return get_location_property(location, LocationProps.value)
