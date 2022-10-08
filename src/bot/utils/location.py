from ..constants.locations import AVAILABLE_LOCATIONS


def is_valid_location(location: str) -> bool:
    return location in AVAILABLE_LOCATIONS
